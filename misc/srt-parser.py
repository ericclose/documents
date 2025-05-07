import re
import argparse # 导入 argparse 模块

def parse_srt_file(srt_file_path):
    """
    解析 SRT 文件并返回一个包含字幕条目的列表。
    每个条目是一个字典，包含 'index', 'time', 和 'text'。
    """
    try:
        with open(srt_file_path, 'r', encoding='utf-8') as f:
            srt_content = f.read()
    except FileNotFoundError:
        print(f"错误：文件 '{srt_file_path}' 未找到。请检查文件路径是否正确。")
        return None
    except Exception as e:
        print(f"读取文件时发生错误：{e}")
        return None

    # 使用正则表达式匹配每个字幕块
    # 匹配序号、时间轴和文本
    # re.DOTALL 使得 '.' 可以匹配换行符
    # re.MULTILINE 使得 '^' 和 '$' 可以匹配每一行的开始和结束
    subtitle_blocks = re.findall(
        r'(\d+)\s*(\d{2}:\d{2}:\d{2},\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2},\d{3})\s*([\s\S]*?)(?=\n\n|\Z)',
        srt_content,
        re.MULTILINE
    )

    subtitles = []
    for block in subtitle_blocks:
        index = int(block[0])
        start_time = block[1]
        end_time = block[2]
        text = block[3].strip() # 去除文本两端的空白字符
        subtitles.append({
            'index': index,
            'time': f"{start_time} --> {end_time}",
            'text': text
        })
    return subtitles

def extract_indexes(subtitles):
    """从解析后的字幕数据中提取所有序号。"""
    if subtitles is None:
        return []
    return [sub['index'] for sub in subtitles]

def extract_timestamps(subtitles):
    """从解析后的字幕数据中提取所有时间轴。"""
    if subtitles is None:
        return []
    return [sub['time'] for sub in subtitles]

def extract_texts(subtitles):
    """从解析后的字幕数据中提取所有字幕文本。"""
    if subtitles is None:
        return []
    return [sub['text'] for sub in subtitles]

# --- 主程序 ---
if __name__ == "__main__":
    # 1. 设置命令行参数解析器
    parser = argparse.ArgumentParser(description="从 SRT 字幕文件中提取序号、时间轴和文本。")
    parser.add_argument("srt_file", help="SRT 字幕文件的路径") # 定义一个必需的位置参数
    parser.add_argument("--extract", choices=['indexes', 'timestamps', 'texts', 'all'], default='all',
                        help="选择要提取的内容: 'indexes', 'timestamps', 'texts', 或 'all' (默认: all)")

    # 2. 解析命令行参数
    args = parser.parse_args()
    srt_file_path = args.srt_file # 获取 SRT 文件路径参数
    extract_choice = args.extract # 获取提取选项

    # 3. 解析 SRT 文件
    parsed_subtitles = parse_srt_file(srt_file_path)

    if parsed_subtitles:
        # 4. 根据选择提取并打印信息
        if extract_choice == 'indexes' or extract_choice == 'all':
            indexes = extract_indexes(parsed_subtitles)
            print("--- 序号 ---")
            for index in indexes:
                print(index)
            print("\n")

        if extract_choice == 'timestamps' or extract_choice == 'all':
            timestamps = extract_timestamps(parsed_subtitles)
            print("--- 时间轴 ---")
            for ts in timestamps:
                print(ts)
            print("\n")

        if extract_choice == 'texts' or extract_choice == 'all':
            texts = extract_texts(parsed_subtitles)
            print("--- 字幕文本 ---")
            for text in texts:
                print(text)
            print("\n")

        # (可选) 如果需要，也可以访问单个字幕条目的所有信息
        # print("--- 单个字幕条目示例 (第一个) ---")
        # if parsed_subtitles and (extract_choice == 'all' or extract_choice == 'debug'): # 假设有一个debug选项
        #     print(f"序号: {parsed_subtitles[0]['index']}")
        #     print(f"时间轴: {parsed_subtitles[0]['time']}")
        #     print(f"文本: {parsed_subtitles[0]['text']}")
    else:
        print(f"未能解析字幕文件: {srt_file_path}")