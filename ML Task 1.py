{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6cf180ed-9faf-4eb4-bffc-edd190faf4fd",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "<>:33: SyntaxWarning: invalid escape sequence '\\<'\n",
      "<>:33: SyntaxWarning: invalid escape sequence '\\<'\n",
      "C:\\Users\\Puppy\\AppData\\Local\\Temp\\ipykernel_12088\\664999830.py:33: SyntaxWarning: invalid escape sequence '\\<'\n",
      "  text = re.sub(\"\\<(.*?)\\>', '\", text)\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import requests\n",
    "import re\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "\n",
    "# function to get the html source text of the medium article\n",
    "def get_page():\n",
    "    global url\n",
    "\n",
    "    # Ask the user to input the URL\n",
    "    url = input(\"Enter url of a medium article: \")\n",
    "\n",
    "    # Handling possible error\n",
    "    if not re.match(r'https?://medium.com/', url):\n",
    "        print('Please enter a valid website, or make sure it is a medium article')\n",
    "        sys.exit(1)\n",
    "\n",
    "    # Get method in requests to fetch the HTML\n",
    "    res = requests.get(url)\n",
    "\n",
    "    res.raise_for_status()\n",
    "    soup = BeautifulSoup(res.text, 'html.parser')\n",
    "    return soup\n",
    "\n",
    "\n",
    "# Function to remove all the HTML tags and replace some with specific strings\n",
    "def clean(text):\n",
    "    rep = {\"<br>\": \"\\n\", \"<br/>\": \"\\n\", \"<li>\": \"\\n\"}\n",
    "    rep = dict((re.escape(k), v) for k, v in rep.items())\n",
    "    pattern = re.compile(\"|\".join(rep.keys()))\n",
    "    text = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)\n",
    "    text = re.sub(\"\\<(.*?)\\>', '\", text)\n",
    "    return text\n",
    "\n",
    "\n",
    "# Function to collect text from the article\n",
    "def collect_text(soup):\n",
    "    text = f'url: {url}\\n\\n'\n",
    "    para_text = soup.find_all('p')\n",
    "    print(f\"paragraphs text = \\n {para_text}\")\n",
    "    for para in para_text:\n",
    "        text += f\"{para.text}\\n\\n\"\n",
    "    return text\n",
    "\n",
    "\n",
    "# Function to save the text into a file in the current directory\n",
    "def save_file(text):\n",
    "    if not os.path.exists('./scraped_articles'):\n",
    "        os.mkdir('./scraped_articles')\n",
    "    name = url.split(\"/\")[-1]\n",
    "    print(name)\n",
    "    fname = f'scraped_articles/{name}.txt'\n",
    "\n",
    "    # Write to file\n",
    "    with open(fname, 'w', encoding='utf-8') as f:\n",
    "        f.write(text)\n",
    "\n",
    "    print(f'File saved in directory {fname}')\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    text = collect_text(get_page())\n",
    "    save_file(text)\n",
    "    # Instructions to Run this python code\n",
    "    # Give url as https://medium.com/@subashgandyer/papa-what-is-a-neural-network-c5e5cc427c7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "95013377-25b7-47a7-85dc-00d4e8b0803a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
