# Requirements:
<pre>pip install cryptography</pre>

# Usage:
<pre>
python Run.py -en input_file output_file
python Run.py -de input_file output_file
python Run.py -en input_file output_file -k key
python Run.py -de input_file output_file -k key
</pre>

# Example:
<pre>
python Run.py -en file.txt file.xyz
python Run.py -de file.xyz file.txt
python Run.py -en file.txt file.xyz -k 12345678901234567890123456789012
python Run.py -de file.xyz file.txt -k 12345678901234567890123456789012
</pre>

# Info:
The program uses AES-256 encryption, the key is generated randomly with each encryption.
After encryption, the console gives you a key that you need to copy and save.
Option -k, --key must have 32 characters, Additionally, the program provides a second key, both keys work for decryption.
During decryption, the console will ask you for the key that was used to encrypt the file.
You can encrypt any file you want, even a photo. And save to whatever file extension you want: .xyz, .zzzz, .dktvq, .file, etc.

![](https://github.com/zbirow/Shz/blob/main/Shz.gif)
