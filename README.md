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

## Finnish

No Finnish file is published. Finnish uses Whisper small. How to rebuild the larger whisper-medium-finnish file (source revision, licence, quantisation, digest) is in <https://github.com/0z00z0/pactrac/issues/402>.

## French: `whisper-small-cv11-french-q5_0.bin`

- **Source**: whisper-small-cv11-french by Bofeng Huang,
  <https://huggingface.co/bofenghuang/whisper-small-cv11-french>, revision
  `83d7df2928fb2218721c543dcc0be29ef8db2f96` (`pytorch_model.bin`, SHA-256
  `855a879fa3a71e75f29ed59fcfce287cf21bcdaab23530cd6f8c4ad192677afb`).
- **Licence**: Apache 2.0, full text in `LICENSES/Apache-2.0.txt`.
- **Changes**: converted to ggml and quantised to q5_0.

## How the files are made

- whisper.cpp at commit `51c6961c7b64b406833f4b6a4a20e67142f69225` (v1.7.5), built with CMake.
- `models/convert-h5-to-ggml.py <source> <openai-whisper> <out>`, with
  the mel filters from openai/whisper at `31243bad24cc746f07d4c8bfdd2d974872cb1803` (v20250625).
- `quantize <in> <out> q5_0` for both.
- The French source's `vocab.json` lacks the text of one special token, which makes its file
  17 bytes shorter than the other small models; whisper.cpp names that token itself.
