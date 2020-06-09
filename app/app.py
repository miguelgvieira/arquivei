# -*- coding: utf-8 -*-

# ------------------------------------
# Imports
# ------------------------------------

import logging

import project

logging.debug("Iniciando servidor Flask")

app = project.create_app()

# ------------------------------------
# 'Main'
# ------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
