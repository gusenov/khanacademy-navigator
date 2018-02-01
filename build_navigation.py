import json
from array import array
import time
import utils

result = None
cnt = None

start_time = time.time()

tabs = []
for idx in range(0, 100):
    tabs.append(idx * '    ')


def walk(node, tab_cnt):
    global result, tabs, cnt

    node_id = node["id"] if "id" in node else ""
    title = node["title"] if "title" in node else ""
    ka_url = node["ka_url"] if "ka_url" in node else ""
    kind = node["kind"] if "kind" in node else ""

    pictograph = ''
    if kind == "Video":
        pictograph = '🎥 '
        cnt["video"]["items"] += 1
        cnt["video"]["ids"][node_id] = True

    result.frombytes((tabs[tab_cnt] + '<li id="' + node_id + '"><a href="' + ka_url + '">' + pictograph + title + "</a>").encode())

    if "children" in node and len(node["children"]) > 0:
        result.frombytes(("\n" + tabs[tab_cnt + 1] + "<ul>\n").encode())
        for child in node["children"]:
            walk(child, tab_cnt + 2)
        result.frombytes((tabs[tab_cnt + 1] + "</ul>\n" + tabs[tab_cnt] + "</li>\n").encode())

    elif "id" in node or "title" in node or "ka_url" in node:
        result.frombytes("</li>\n".encode())


def run(input_file, output_file):
    print(input_file, "->", output_file)

    global result, cnt
    result = array('b')
    cnt = {"video": {"items": 0, "ids": {}}}

    with open(input_file, "r") as f:
        topic_tree = json.load(f)

    result.frombytes("<ul>".encode())
    walk(topic_tree, 0)
    result.frombytes("</ul>".encode())

    with open(output_file, "w") as out:
        out.write(result.tobytes().decode())

    print("🎥 items count:", cnt["video"]["items"])
    print("🎥 ids count:", len(cnt["video"]["ids"]))


def all_subjects():
    utils.silentremove("Topics and Exercises.html")
    run("api/v1/topictree/Topics and Exercises.json", "Topics and Exercises.html")

    utils.silentremove("Topics only.html")
    run("api/v1/topictree/Topics only.json", "Topics only.html")

    utils.silentremove("topictree.html")
    run("api/v1/topictree/topictree.json", "topictree.html")


def math():
    utils.silentremove("Math Topics and Exercises.html")
    run("api/v1/topictree/Math Topics and Exercises.json", "Math Topics and Exercises.html")

    utils.silentremove("Math Topics only.html")
    run("api/v1/topictree/Math Topics only.json", "Math Topics only.html")

    utils.silentremove("Math topictree.html")
    run("api/v1/topictree/Math topictree.json", "Math topictree.html")


# all_subjects()
math()

print("--- %s seconds ---" % (time.time() - start_time))
