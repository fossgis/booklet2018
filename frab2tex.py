#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import sys, os, csv

tnListen = {}

with open(sys.argv[1], "r") as r:
    reader = csv.reader(r)
    # 0, 1,        2,         3,    4,    5,      6,           7,       8,   9,   10,        11
    # id,last_name,first_name,email,title,subtitle,description,abstract,name,room,start_time,type
    # 0, 1,    2,   3,    4,       5,          6,       7,         8
    # id,email,name,title,subtitle,description,abstract,start_time,name
    
    talk_rows = []
    for row in reader:
        if row[0] == "id":
            continue
        talk_rows.append(row)
    
    talk_rows.sort(key=lambda r: r[10])
    for row in talk_rows:
        room = row[9]
        sys.stdout.write("% time: {}\n".format(row[10]))
        sys.stdout.write("\\noindent")
        if row[11] == "workshop":
            sys.stdout.write("\\workshop{" + row[4] + "}{" + row[2] + " " + row[1] + "}%\n{" + row[9] + "}\workshopspace")
        elif row[8] == "Wolfgang-Paul-Hörsaal":
            sys.stdout.write("\\abstractWPH{" + row[2] + " " + row[1] + "}%\n{" + row[4] + "}%\n{" + row[5] + "}%\n{%\n" + row[7].strip() + "%\n}\n")
        elif row[8] == "Alfred-Philippson-Hörsaal":
            sys.stdout.write("\\abstractAPH{" + row[2] + " " + row[1] + "}%\n{" + row[4] + "}%\n{" + row[5] + "}%\n{%\n" + row[7].strip() + "%\n}\n")
        elif row[8] == "Hörsaal IV - Geozentrum":
            sys.stdout.write("\\abstractVier{" + row[2] + " " + row[1] + "}%\n{" + row[4] + "}%\n{" + row[5] + "}%\n{%\n" + row[7].strip() + "%\n}\n")
        elif row[8] == "Hörsaal II - Geozentrum":
            sys.stdout.write("\\abstractZwei{" + row[2] + " " + row[1] + "}%\n{" + row[4] + "}%\n{" + row[5] + "}%\n{%\n" + row[7].strip() + "%\n}\n")
        else:
            sys.stdout.write("\\abstractOther{" + row[2] + " " + row[1] + "}%\n{" + row[4] + "}%\n{" + row[5] + "}%\n{%\n" + row[7].strip() + "%\n}{" + row[9] +  "}\n")
        sys.stdout.write("\n\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n")

