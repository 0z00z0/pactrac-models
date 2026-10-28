# pactrac-models

Speech models for PacTrac's on-device dictation, in the ggml form whisper.cpp reads. Each file is a
conversion of a model published by someone else, made because no file in this form exists at the
source. The files are release assets under the tag `2026-10-28`; this repository holds no code of
its own.

Each file keeps its source's licence. The conversion changes the file format and the precision of
the weights, nothing else.

## Files

| File | Bytes | SHA-256 |
|---|---|---|
| `pallr-whisper-small-is-q5_0.bin` | 175 209 680 | `74a42d71e950e295e862ee4f2055f7151c11aba46aab845ef03f2c9b4f074da9` |
| `whisper-medium-finnish-q5_0.bin` | 539 212 467 | `b410f4a4c1cf37c02387cde83923fd2ebe84e69c4955fe0f5fc5cb89395d66a4` |
| `whisper-small-cv11-french-q5_0.bin` | 175 209 663 | `d5a0803b6e04a93cf1c906f048b0b964265c40226595d8e70db7b2dec4d157a6` |

## Icelandic: `pallr-whisper-small-is-q5_0.bin`

- **Source**: pallr-whisper-small-is by Páll Rúnarsson, HUMI lab, Reykjavík University,
  <https://huggingface.co/palli23/pallr-whisper-small-is>, revision
  `25104cec2fee3679ba474459ba866ad47407ca60` (`model.safetensors`, SHA-256
  `54e9d7415ba51c036218da0c2126f7e5ab15e1a302602b2c588078c6c7a1a795`).
- **Licence**: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0),
  <https://creativecommons.org/licenses/by-sa/4.0/>, full text in `LICENSES/CC-BY-SA-4.0.txt`.
  This converted file is shared under the same licence.
- **Changes**: converted to ggml and quantised to q5_0. The source carries no `vocab.json`;
  `convert/derive-vocab-from-tokenizer.py` writes it from the source's own `tokenizer.json`.
- Provided as-is, without warranties of any kind. The source's author does not endorse this
  conversion.

## Finnish: `whisper-medium-finnish-q5_0.bin`

- **Source**: whisper-medium-finnish by Finnish-NLP, <https://huggingface.co/Finnish-NLP/whisper-medium-finnish>,
  in Finnish-NLP's own ggml form: `ggml-model-fi-medium.bin` from
  <https://huggingface.co/Finnish-NLP/Finnish-finetuned-whisper-models-ggml-format>, revision
  `c58924b6deb4438756b3d38ecd67d65bdf20298d` (SHA-256
  `a0d1126381bebc9155e6a06a36ae4bf8e87abd02eacf73fff1593719a7d6c739`).
- **Licence**: Apache 2.0, full text in `LICENSES/Apache-2.0.txt`.
- **Changes**: quantised from f16 to q5_0.

## French: `whisper-small-cv11-french-q5_0.bin`

- **Source**: whisper-small-cv11-french by Bofeng Huang,
  <https://huggingface.co/bofenghuang/whisper-small-cv11-french>, revision
  `83d7df2928fb2218721c543dcc0be29ef8db2f96` (`pytorch_model.bin`, SHA-256
  `855a879fa3a71e75f29ed59fcfce287cf21bcdaab23530cd6f8c4ad192677afb`).
- **Licence**: Apache 2.0, full text in `LICENSES/Apache-2.0.txt`.
- **Changes**: converted to ggml and quantised to q5_0.

## How the files are made

- whisper.cpp at commit `51c6961c7b64b406833f4b6a4a20e67142f69225` (v1.7.5), built with CMake.
- `models/convert-h5-to-ggml.py <source> <openai-whisper> <out>` for Icelandic and French, with
  the mel filters from openai/whisper at `31243bad24cc746f07d4c8bfdd2d974872cb1803` (v20250625).
- `quantize <in> <out> q5_0` for all three.
- The French source's `vocab.json` lacks the text of one special token, which makes its file
  17 bytes shorter than the other small models; whisper.cpp names that token itself.
