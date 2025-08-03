import os
import time
import ffmpeg  # For audio extraction
from faster_whisper import WhisperModel
from tqdm import tqdm

# --- Configuration ---
VIDEO_FILE = "media.mp4"
MODEL_SIZE = "large-v3"
DEVICE = "cuda"
# Use float16 for better performance on modern GPUs
COMPUTE_TYPE = "float16" 
# ---------------------

def format_timestamp(seconds: float) -> str:
    """
    Converts a timestamp in seconds to the SRT format (HH:MM:SS,ms).
    
    Args:
        seconds (float): The timestamp in seconds.
        
    Returns:
        str: The formatted timestamp string.
    """
    assert seconds >= 0, "non-negative timestamp expected"
    milliseconds = round(seconds * 1000.0)

    hours = milliseconds // 3_600_000
    milliseconds %= 3_600_000

    minutes = milliseconds // 60_000
    milliseconds %= 60_000

    seconds = milliseconds // 1_000
    milliseconds %= 1_000

    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

def generate_srt(segments, output_file: str):
    """
    Generates a SubRip (.srt) file from the transcribed segments.
    
    Args:
        segments (iterator): The segments iterator from WhisperModel.
        output_file (str): The path to the output SRT file.
    """
    with open(output_file, 'w', encoding='utf-8') as srt_file:
        for i, segment in enumerate(segments):
            start_time = format_timestamp(segment.start)
            end_time = format_timestamp(segment.end)
            text = segment.text.strip()
            
            srt_file.write(f"{i + 1}\n")
            srt_file.write(f"{start_time} --> {end_time}\n")
            srt_file.write(f"{text}\n\n")

def main():
    """
    Main function to run the video transcription process.
    """
    # --- 1. Check for Video File ---
    if not os.path.exists(VIDEO_FILE):
        print(f"Error: Video file not found at '{VIDEO_FILE}'")
        return

    # --- 2. Extract Audio from Video ---
    print(f"Extracting audio from '{VIDEO_FILE}'...")
    audio_file_temp = "temp_audio.wav"
    try:
        # Use ffmpeg-python to extract audio, resample to 16kHz (required by Whisper)
        # and convert to mono WAV format.
        (
            ffmpeg
            .input(VIDEO_FILE)
            .output(audio_file_temp, acodec='pcm_s16le', ac=1, ar='16k')
            .run(overwrite_output=True, quiet=True)
        )
        print("Audio extraction complete.")
    except ffmpeg.Error as e:
        print(f"Error during audio extraction: {e.stderr.decode()}")
        return

    # --- 3. Load the Whisper Model ---
    print(f"Loading Whisper model '{MODEL_SIZE}' on device '{DEVICE}'...")
    try:
        model = WhisperModel(MODEL_SIZE, device=DEVICE, compute_type=COMPUTE_TYPE)
        print("Model loaded successfully.")
    except Exception as e:
        print(f"Error loading model: {e}")
        if os.path.exists(audio_file_temp):
            os.remove(audio_file_temp)
        return

    # --- 4. Transcribe the Audio with Progress Visualization ---
    print("Transcribing audio... (This may take a while)")
    start_time = time.time()
    
    # The transcribe method returns an iterator and an info object
    segments_iterator, info = model.transcribe(
        audio_file_temp,
        beam_size=5,
        word_timestamps=False, # Set to True if you need word-level timestamps
    )

    print(f"Detected language '{info.language}' with probability {info.language_probability:.2f}")
    print(f"Audio duration: {format_timestamp(info.duration)}")

    # Create a list from the iterator to process and show progress
    segments_list = []
    
    # Use tqdm to create a progress bar
    # The total is the audio duration in seconds
    with tqdm(total=round(info.duration), unit="sec", desc="Transcription Progress") as pbar:
        last_progress_update = 0
        for segment in segments_iterator:
            segments_list.append(segment)
            # Update progress bar based on the end time of the current segment
            pbar.update(round(segment.end - last_progress_update))
            last_progress_update = segment.end
        
        # Ensure the progress bar reaches 100% at the end
        if last_progress_update < info.duration:
             pbar.update(round(info.duration - last_progress_update))


    transcription_time = time.time() - start_time
    print(f"Transcription finished in {transcription_time:.2f} seconds.")

    # --- 5. Generate SRT Subtitle File ---
    srt_output_file = os.path.splitext(VIDEO_FILE)[0] + ".srt"
    print(f"Generating SRT file: '{srt_output_file}'...")
    generate_srt(segments_list, srt_output_file)
    print("SRT file generated successfully.")

    # --- 6. Cleanup ---
    print("Cleaning up temporary audio file...")
    if os.path.exists(audio_file_temp):
        os.remove(audio_file_temp)
    print("Process complete.")


if __name__ == "__main__":
    main()