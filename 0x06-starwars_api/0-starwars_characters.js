#!/usr/bin/node

const request = require('request');
const util = require('util');

const reqPromise = util.promisify(request);

async function getCharacters () {
  const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

  try {
    const { body } = await reqPromise(url);
    const data = JSON.parse(body);

    for (let i = 0; i < data.characters.length; i++) {
      const character = await reqPromise(data.characters[i]);
      console.log(JSON.parse(character.body).name);
    }
  } catch (err) {
    console.log(err);
  }
}

getCharacters();
