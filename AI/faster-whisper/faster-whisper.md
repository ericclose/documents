## Requirements

* [Python](https://www.python.org/downloads/)
* [PyTorch](https://pytorch.org/get-started/locally/) (recommended CUDA version)
* cuBLAS (included in the [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit-archive))
* [cuDNN 9.x](https://developer.nvidia.com/cudnn)
* ~[cuDNN 8.x](https://developer.nvidia.com/rdp/cudnn-archive) / [redist link](https://developer.download.nvidia.com/compute/cudnn/redist/cudnn/windows-x86_64/)~
  * ~system path: `C:\Program Files\Nvidia\CUDNN\v8.x`~
 
> **Note**: The latest versions of `ctranslate2` only support CUDA 12 and cuDNN 9. For CUDA 11 and cuDNN 8, the current workaround is downgrading to the `3.24.0` version of `ctranslate2`, for CUDA 12 and cuDNN 8, downgrade to the `4.4.0` version of `ctranslate2`, (This can be done with `pip install --force-reinstall ctranslate2==4.4.0` or specifying the version in a `requirements.txt`).
>
> Ref. [SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper?tab=readme-ov-file#gpu)

## Installation

The module can be installed from PyPI:

```bash
pip install faster-whisper
```
