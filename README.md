# 🚫 Profanity Filter for Chinese Social Media —— Variant Detection with Word Embeddings

This project aims to address the problem of profanities and their creative variants on Chinese social media platforms.  
Traditional keyword filters can be easily bypassed, e.g., “傻逼” (idiot) may appear as “煞笔”, “傻比”, “傻b”, etc.  
This project leverages **word embeddings (word2vec)** to recognize and filter such variants, improving accuracy and robustness.  

---

## 📖 Background
On platforms like Bilibili and Douyin, user comments often contain offensive language.  
Existing methods include:
- Keyword filtering
- Sentiment analysis
- Human moderation
- Machine Learning & NLP

However, the **variant phenomenon** in Chinese (homophones, character substitutions) makes detection more challenging compared to English .

---

## 🎯 Objective
- Detect Chinese profanity and its disguised variants  
- Automatically screen comments containing inappropriate language  
- Provide a cleaner and healthier online environment  

---

## 🛠️ Methodology
1. **Corpus**: Tencent AI Lab Chinese word embeddings (100/200 dimensions, millions of words)  
2. **Target Words**: Selected typical profanities (“傻逼”, “操”)  
3. **Model Loading**: Using `gensim` to load embeddings  
4. **Variant Detection**: `most_similar()` function to find semantically close variants  

---
## 📊 Results
- Successfully identified multiple variants of “傻逼” and “操”
- Demonstrated the effectiveness of word embeddings for detecting disguised Chinese profanity

---

## 🚀 Future Work
- Integrate larger corpora
- Expand to more categories of sensitive words
- Combine with sentiment analysis and deep learning models for improved accuracy

---

## 🙌 Acknowledgments

Special thanks to Prof. Elaine Uí Dhonnchad for assistance in corpus searching.
Corpus reference: [Tencent AI Lab Embedding](https://metatext.io/datasets/tencent-ai-lab-embedding-corpus)

---

Example results:  
```python
>>> w2v_model.most_similar("傻逼", topn=5)
[('煞笔', 0.9753), ('傻比', 0.9524), ('傻逼啊', 0.9431), ('傻b', 0.9292), ('大傻逼', 0.9223)]

>>> w2v_model.most_similar("操", topn=5)
[('妈的', 0.7752), ('狗日的', 0.7749), ('他娘的', 0.7738), ('他妈的', 0.7730), ('我操', 0.7590)]
