import os

if __name__ == '__main__':
    output = []
    with open("anime.md", "r") as file:
        lines = file.readlines()
        for line in lines[2:]:
            tokens = line.split("|")
            anime = tokens[2].strip()
            converted = anime.lower().replace(" ", "_")
            filepath = f'images/{anime}.png'
            print(filepath)
            if os.path.exists(filepath):
                os.popen(f'copy {filepath} processed/{converted}.png')
                tokens[1] = f'![](https://raw.githubusercontent.com/branyoto/seen/main/images/{converted})'
            output.append('|'.join(tokens))

    with open("tmp.md", "w") as file:
        file.write("".join(output))
