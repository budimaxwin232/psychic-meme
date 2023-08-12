import random
import string
import requests
import time
from threading import Thread

def generate_random_domain():
    prefixes = open('common_words.dat').read ().splitlines()
    common_words = open('common_words.dat').read ().splitlines()
    suffixes = open('common_words.dat').read ().splitlines()
    
    while True:
        random_prefix = random.choice(prefixes)
        random_word = random.choice(common_words)
        random_suffix = random.choice(suffixes)
        random_chars = ''.join(random.choices(string.ascii_lowercase, k=3))
        random_number = random.randint(100, 999)
        random_tld = random.choice([".net", ".com", ".org"])
        
        domain = f"{random_prefix}{random_word}{random_tld}"
        yield domain

def main():
    class c1(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c2(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c3(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c4(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c5(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c6(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c7(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c8(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c9(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c10(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c11(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c12(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c13(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c14(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c15(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c16(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c17(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c18(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c19(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c20(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c21(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c22(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c23(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c24(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c25(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c26(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c27(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c28(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c29(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c30(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c31(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c32(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c33(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c34(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c35(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c36(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c37(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c38(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c39(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c40(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c41(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c42(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c43(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c44(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c45(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c46(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c47(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c48(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c49(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c50(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c51(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c52(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c53(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c54(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c55(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c56(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c57(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c58(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c59(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c60(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c61(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c62(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c63(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c64(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c65(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c66(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c67(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c68(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c69(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c70(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c71(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c72(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c73(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c74(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c75(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c76(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c77(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c78(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c79(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c80(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c81(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c82(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c83(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c84(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c85(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c86(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c87(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c88(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c89(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c90(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c91(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c92(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c93(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c94(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c95(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c96(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c97(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c98(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c99(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                        
    class c100(Thread):
        def run(self):
            domain_generator = generate_random_domain()
            while True:
                domain = next(domain_generator)
                if is_domain_active(domain):
                    print(f"Active Domain Found: {domain}")
                    
                    with open('found.txt', 'a+') as fp:
                        fp.write(domain + '\n')
                
    t1 = c1()
    t2 = c2()
    t3 = c3()
    t4 = c4()
    t5 = c5()
    t6 = c6()
    t7 = c7()
    t8 = c8()
    t9 = c9()
    t10 = c10()
    t11 = c11()
    t12 = c12()
    t13 = c13()
    t14 = c14()
    t15 = c15()
    t16 = c16()
    t17 = c17()
    t18 = c18()
    t19 = c19()
    t20 = c20()
    t21 = c21()
    t22 = c22()
    t23 = c23()
    t24 = c24()
    t25 = c25()
    t26 = c26()
    t27 = c27()
    t28 = c28()
    t29 = c29()
    t30 = c30()
    t31 = c31()
    t32 = c32()
    t33 = c33()
    t34 = c34()
    t35 = c35()
    t36 = c36()
    t37 = c37()
    t38 = c38()
    t39 = c39()
    t40 = c40()
    t41 = c41()
    t42 = c42()
    t43 = c43()
    t44 = c44()
    t45 = c45()
    t46 = c46()
    t47 = c47()
    t48 = c48()
    t49 = c49()
    t50 = c50()
    t51 = c51()
    t52 = c52()
    t53 = c53()
    t54 = c54()
    t55 = c55()
    t56 = c56()
    t57 = c57()
    t58 = c58()
    t59 = c59()
    t60 = c60()
    t61 = c61()
    t62 = c62()
    t63 = c63()
    t64 = c64()
    t65 = c65()
    t66 = c66()
    t67 = c67()
    t68 = c68()
    t69 = c69()
    t70 = c70()
    t71 = c71()
    t72 = c72()
    t73 = c73()
    t74 = c74()
    t75 = c75()
    t76 = c76()
    t77 = c77()
    t78 = c78()
    t79 = c79()
    t80 = c80()
    t81 = c81()
    t82 = c82()
    t83 = c83()
    t84 = c84()
    t85 = c85()
    t86 = c86()
    t87 = c87()
    t88 = c88()
    t89 = c89()
    t90 = c90()
    t91 = c91()
    t92 = c92()
    t93 = c93()
    t94 = c94()
    t95 = c95()
    t96 = c96()
    t97 = c97()
    t98 = c98()
    t99 = c99()
    t100 = c100()

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()
    t15.start()
    t16.start()
    t17.start()
    t18.start()
    t19.start()
    t20.start()
    t21.start()
    t22.start()
    t23.start()
    t24.start()
    t25.start()
    t26.start()
    t27.start()
    t28.start()
    t29.start()
    t30.start()
    t31.start()
    t32.start()
    t33.start()
    t34.start()
    t35.start()
    t36.start()
    t37.start()
    t38.start()
    t39.start()
    t40.start()
    t41.start()
    t42.start()
    t43.start()
    t44.start()
    t45.start()
    t46.start()
    t47.start()
    t48.start()
    t49.start()
    t50.start()
    t51.start()
    t52.start()
    t53.start()
    t54.start()
    t55.start()
    t56.start()
    t57.start()
    t58.start()
    t59.start()
    t60.start()
    t61.start()
    t62.start()
    t63.start()
    t64.start()
    t65.start()
    t66.start()
    t67.start()
    t68.start()
    t69.start()
    t70.start()
    t71.start()
    t72.start()
    t73.start()
    t74.start()
    t75.start()
    t76.start()
    t77.start()
    t78.start()
    t79.start()
    t80.start()
    t81.start()
    t82.start()
    t83.start()
    t84.start()
    t85.start()
    t86.start()
    t87.start()
    t88.start()
    t89.start()
    t90.start()
    t91.start()
    t92.start()
    t93.start()
    t94.start()
    t95.start()
    t96.start()
    t97.start()
    t98.start()
    t99.start()
    t100.start()

def is_domain_active(domain):
    try:
        response = requests.get(f"http://{domain}")
        return response.status_code
    except Exception as e:print(e);return False
        
if __name__=="__main__":
	start_time = time.time()
	main()
	
	end_time = time.time() - start_time
	
	print(end_time)