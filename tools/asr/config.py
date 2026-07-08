def get_models():
    model_size_list = [
        "medium",
        "medium.en",
        "large-v2",
        "large-v3",
        "large-v3-turbo",
    ]
    return model_size_list


asr_dict = {
    "SenseVoice (极速, 5语种, 推荐)": {"lang": ["zh", "en", "ja", "ko", "yue", "auto"], "size": ["large"], "path": "funasr_asr.py", "precision": ["float32"], "backend": "sensevoice"},
    "Fun-ASR-Nano (31语种+方言)": {"lang": ["zh", "en", "ja", "ko", "yue", "auto"], "size": ["large"], "path": "funasr_asr.py", "precision": ["float32"], "backend": "fun-asr-nano"},
    "达摩 ASR (中文经典)": {"lang": ["zh", "yue"], "size": ["large"], "path": "funasr_asr.py", "precision": ["float32"], "backend": "damo"},
    "Faster Whisper (多语种)": {
        "lang": ["auto", "en", "ja", "ko"],
        "size": get_models(),
        "path": "fasterwhisper_asr.py",
        "precision": ["float32", "float16", "int8"],
    },
}
