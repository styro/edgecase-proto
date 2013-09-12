#!/usr/bin/python

import itertools
import xml.etree.ElementTree as etree

def parse_links(filename):
    tree = etree.parse(filename)
    posts = tree.findall('post')
    return [post.attrib for post in posts]

    
def process_tags(posts):
    data = {}
    for post in posts:
        tags = post['tag'].split(' ')
        for tag1, tag2 in itertools.permutations(tags,2):
            if tag1 in data:
                if tag2 in data[tag1]:
                    data[tag1][tag2] += 1
                else:
                    data[tag1][tag2] = 1
            else:
                data[tag1] = {tag2: 1}
    return data

def top_connections(data, num=10):
    connections = {}
    top_ranks = [1]
    for tag, connected_tags in data.iteritems():
        for connected_tag, connection_count in connected_tags.iteritems():
            print top_ranks
            pair = [tag, connected_tag]
            pair.sort()
            pair = tuple(pair)
            if pair not in connections:
                if connection_count > min(top_ranks):
                    connections[pair] = connection_count
                    top_ranks.append(connection_count)
                    if len(top_ranks) > num:
                        top_ranks.sort(reverse=True)
                        top_ranks = top_ranks[:num]
    return dict([(x, connections[x]) for x in connections if connections[x] >=
        min(top_ranks)])


if __name__ == '__main__':
    default_data = 'all.xml'
    posts = parse_links(default_data)
    data = process_tags(posts)

