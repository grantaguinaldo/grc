from flask import Flask, jsonify, request, render_template
import pandas as pd
import sqlalchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, create_engine, MetaData
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

app = Flask(__name__)

connection_string = 'sqlite:///grc_files.sqlite'
engine = create_engine(connection_string)
Base = automap_base()
Base.prepare(engine, reflect=True)
grc_2019 = Base.classes.grc_2019
session = Session(engine)
conn = engine.connect()
Base.classes.keys()


@app.route('/is_alive')
def is_alive():
  return 'I am alive!'


@app.route('/api', methods=['GET'])
def api_function():

  entry_id = request.args.get('fileidx')

  QUERY_RESPONSE = session.query(grc_2019.file_index,
                                 grc_2019.file_name,
                                 grc_2019.file_url,
                                 grc_2019.file_text)\
      .filter(grc_2019.file_index == entry_id).all()

  TEMP_DICT = pd.DataFrame(QUERY_RESPONSE).to_dict()

  return jsonify(TEMP_DICT)


if __name__ == '__main__':
  app.run(debug=True)
