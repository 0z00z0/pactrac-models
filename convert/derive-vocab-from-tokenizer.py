# Writes vocab.json (the BPE model vocabulary) and an empty added_tokens.json beside a tokenizer.json.
import json, sys, pathlib
d = pathlib.Path(sys.argv[1])
tok = json.load((d / "tokenizer.json").open(encoding="utf8"))
vocab = tok["model"]["vocab"]
json.dump(vocab, (d / "vocab.json").open("w", encoding="utf8"), ensure_ascii=False)
if not (d / "added_tokens.json").exists():
    (d / "added_tokens.json").write_text("{}")
print("vocab entries", len(vocab))
