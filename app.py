# 1. import Flask
import numpy as np
import os

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify

# 2. Create an app, being sure to pass __name__
# For details on this, see: http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application
app = Flask(__name__)


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")

    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"

    )


# 4. Define what to do when a user hits the /about route
@app.route("/api/v1.0/precipitation")
def precipitation():
    print("query using date as the key and prcp as the value")
    session = Session(engine)
    precip_data = session.query(Measurement.prcp, Measurement.date).filter(Measurement.date >= date).all()

    # close the session to end communication with the server
    session.close()

    
    
    return jsonify(precip_data)



if __name__ == "__main__":
    app.run(debug=True)