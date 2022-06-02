
from random import randint

# # chr()
# """
# 从给定的ASCII代码中查找字符值 
# 返回一个带有序号i的一个字符的Unicode字符串；0<=i<=0x10ffff。 ： 字母97-122 ： a-z
# """

# 随机整数： randint()
# 从3到13个字母 :   随机字母的长度也随机：  "".join([chr(randint(97,122)) for _ in range(randint(3, 13))])
# 从1到100个单词 :  单词个数随机：         ["".join([chr(randint(97,122)) for _ in range(randint(3, 6))]) for _ in range(randint(1, 3))]
# 1000个句子    ：  句子个数固定：         [" ".join(["".join([chr(randint(97,122)) for _ in range(randint(3, 6))]) for _ in range(randint(1, 3))])  for _ in range(5)]                 


# 测试10000次。
L = [' '.join(''.join(chr(randint(97, 122)) 
                for _ in range(randint(3, 13))) 
            for _ in range(randint(1, 100))) 
        for _ in range(1000)] 




