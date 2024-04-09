# Requirements:
<pre>pip install cryptography</pre>

# Usage:
<pre>
python Run.py -en input_file output_file
python Run.py -de input_file output_file
</pre>

#Example
<pre>
python Run.py -en file.txt file.xyz
python Run.py -de file.xyz file.txt
</pre>

The program uses AES-256 encryption, the key is generated randomly with each encryption.
After encryption, the console gives you a key that you need to copy and save.
During decryption, the console will ask you for the key that was used to encrypt the file.

![](https://github.com/zbirow/Shz/edit/main/Shz.gif)
