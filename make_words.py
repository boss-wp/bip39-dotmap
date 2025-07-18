from mnemonic import Mnemonic

mnemo = Mnemonic("english")
wordlist = mnemo.wordlist

while True:
    words = mnemo.generate(strength=256).split() #24个单词
    old_checksum = words[-1]

    words_replace = words.copy()  # ✅ 复制一份独立列表

    words_replace[2 - 1] = 'key' #-1代表替换实际的序列
    words_replace[8 - 1] = 'hello' #-1代表替换实际的序列
    words_replace.pop()
    new_words_replace = " ".join(words_replace)

    for new_checksum in wordlist:
        mnemonic_sentence = new_words_replace + " " + new_checksum
        if mnemo.check(mnemonic_sentence):
            if old_checksum == new_checksum:


                print("======================开始======================")

                for word in words:
                    if word in wordlist:
                        index = wordlist.index(word) + 1
                        binary = bin(index)[2:].zfill(12).replace('0', '○').replace('1', '●')
                        binary_chunks = [binary[i:i+4] for i in range(0, len(binary), 4)]
                        join_binary_chunks = " | ".join(binary_chunks)
                        print(f"{str(index).zfill(4):<8}{word:<9}{join_binary_chunks}")

                print("原文本: ", " ".join(words))

                print("------------------------------------------------")

                for word in words:
                    if word in wordlist:
                        index = wordlist.index(word) + 1
                        binary = bin(index)[2:].zfill(12).replace('0', '○').replace('1', '●')
                        binary_chunks = [binary[i:i+4] for i in range(0, len(binary), 4)]
                        join_binary_chunks = " | ".join(binary_chunks)
                        print(f"{str(index).zfill(4):<8}{word:<9}{join_binary_chunks}")

                print("修改后: ", mnemonic_sentence)
                print("======================结束======================")
                break