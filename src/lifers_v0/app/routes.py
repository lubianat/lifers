from app import app, db
from flask import render_template, redirect, url_for
import os
import yaml
from flask import abort


@app.route("/")
def index():
    directory_path = os.path.join(os.getcwd(), "app/experience_packs")
    experience_packs = []

    for filename in os.listdir(directory_path):
        if filename.endswith(".yaml"):
            with open(os.path.join(directory_path, filename), "r") as f:
                pack_data = yaml.safe_load(f)
                experience_packs.append(
                    (pack_data["pack"]["name"], pack_data["pack"]["id"])
                )

    return render_template("index.html", experience_packs=experience_packs)


@app.route("/pack/<pack_id>")
def pack_details(pack_id):
    directory_path = os.path.join(os.getcwd(), "app/experience_packs")
    pack_data = None

    for filename in os.listdir(directory_path):
        if filename.endswith(".yaml"):
            with open(os.path.join(directory_path, filename), "r") as f:
                current_pack_data = yaml.safe_load(f)
                if current_pack_data["pack"]["id"] == pack_id:
                    pack_data = current_pack_data
                    break

    if not pack_data:
        abort(404)

    return render_template("pack_details.html", pack_data=pack_data)
