Last login: Tue Apr 23 19:43:18 on ttys000
(base) zhangshengjie@zhangshengjiedeMacBook-Air ~ % cd /Users/zhangshengjie/Desktop/Project_Profanity\ Filter
(base) zhangshengjie@zhangshengjiedeMacBook-Air Project_Profanity Filter % curl -o tencent-ailab-embedding-zh-d100-v0.2.0-s.tar.gz https://ai.tencent.com/ailab/nlp/en/data/tencent-ailab-embedding-zh-d100-v0.2.0-s.tar.gz
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  762M  100  762M    0     0  5822k      0  0:02:14  0:02:14 --:--:-- 7644k
(base) zhangshengjie@zhangshengjiedeMacBook-Air Project_Profanity Filter % pip3 install gensim
Requirement already satisfied: gensim in /Users/zhangshengjie/miniconda3/lib/python3.11/site-packages (4.3.2)
Requirement already satisfied: numpy>=1.18.5 in /Users/zhangshengjie/miniconda3/lib/python3.11/site-packages (from gensim) (1.26.3)
Requirement already satisfied: scipy>=1.7.0 in /Users/zhangshengjie/miniconda3/lib/python3.11/site-packages (from gensim) (1.12.0)
Requirement already satisfied: smart-open>=1.8.1 in /Users/zhangshengjie/miniconda3/lib/python3.11/site-packages (from gensim) (6.4.0)
(base) zhangshengjie@zhangshengjiedeMacBook-Air Project_Profanity Filter % python
Python 3.11.5 (main, Sep 11 2023, 08:31:25) [Clang 14.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from gensim.models import KeyedVectors
>>> model_path = "/Users/zhangshengjie/Desktop/Project_Profanity Filter/tencent-ailab-embedding-zh-d100-v0.2.0-s/tencent-ailab-embedding-zh-d100-v0.2.0-s.txt"
>>> w2v_model = KeyedVectors.load_word2vec_format(model_path, binary=False)
print(w2v_model.most_similar("自然语言处理", topn=5))>>> w2v_model = KeyedVectors.lo
>>> print(w2v_model.most_similar("傻逼", topn=5))
[('煞笔', 0.9753351211547852), ('傻比', 0.9524455070495605), ('傻逼啊', 0.9431149959564209), ('傻b', 0.9292600750923157), ('大傻逼', 0.9223935008049011)]
>>> print(w2v_model.most_similar("傻逼", topn=6))
[('煞笔', 0.9753351211547852), ('傻比', 0.9524455070495605), ('傻逼啊', 0.9431149959564209), ('傻b', 0.9292600750923157), ('大傻逼', 0.9223935008049011), ('二逼', 0.9119765162467957)]
>>> print(w2v_model.most_similar("傻逼", topn=10))
[('煞笔', 0.9753351211547852), ('傻比', 0.9524455070495605), ('傻逼啊', 0.9431149959564209), ('傻b', 0.9292600750923157), ('大傻逼', 0.9223935008049011), ('二逼', 0.9119765162467957), ('傻逼吧', 0.9062010049819946), ('臭傻逼', 0.8960307240486145), ('傻叉', 0.8755214810371399), ('那个傻逼', 0.8723161816596985)]
>>> print(w2v_model.most_similar("操", topn=10))
[('妈的', 0.7752609848976135), ('狗日的', 0.7749193906784058), ('他娘的', 0.7738223075866699), ('他妈的', 0.7730444073677063), ('我操', 0.7590153217315674), ('娘的', 0.7562870383262634), ('丫的', 0.754307746887207), ('我呸', 0.7516244649887085), ('操你妈', 0.7483251690864563), ('奶奶个熊', 0.7471296787261963)]
>>> print(w2v_model.most_similar("操", topn=5))
[('妈的', 0.7752609848976135), ('狗日的', 0.7749193906784058), ('他娘的', 0.7738223075866699), ('他妈的', 0.7730444073677063), ('我操', 0.7590153217315674)]
>>> exit()
(base) zhangshengjie@zhangshengjiedeMacBook-Air Project_Profanity Filter % curl -o tencent-ailab-embedding-zh-d100-v0.2.0.tar.gz https://ai.tencent.com/ailab/nlp/en/data/tencent-ailab-embedding-zh-d200-v0.2.0.tar.gz 
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 9127M  100 9127M    0     0  4978k      0  0:31:17  0:31:17 --:--:-- 4459k
(base) zhangshengjie@zhangshengjiedeMacBook-Air Project_Profanity Filter % python
Python 3.11.5 (main, Sep 11 2023, 08:31:25) [Clang 14.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
