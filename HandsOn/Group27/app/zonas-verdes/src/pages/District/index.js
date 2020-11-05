import React, { useEffect, useState, useContext } from 'react';
import { jsonParserFixed } from '../../helpers/fixes';
import { useParams } from 'react-router-dom';

import { ThemeContext } from '../../App';

import {
  graph,
  Namespace,
  Fetcher,
  parse,
  sym,
  //   serialize,
  //   jsonParser,
} from 'rdflib';
import { parse as htmlParser } from 'node-html-parser';

export default function District() {
  const [store, setMystore] = useContext(ThemeContext);

  useEffect(() => {
    let doc = sym('http://api.zonasVerdesMadrid.com');
    setMystore(
      '<http://api.zonasverdesmadrid.com/resources/districts/Centro> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://api.zonasVerdesMadrid.com/ontologies#district>.',
      doc.uri,
      'text/n3'
    );
  }, []);
  const ONT = new Namespace('http://api.zonasVerdesMadrid.com/ontologies/');
  const OWL = new Namespace('http://www.w3.org/2002/07/owl');

  const { districtId } = useParams();

  const [loading, setloading] = useState(true);

  const myDistrict = store
    .match(null, ONT('districts#hasName'), districtId)
    .map(({ subject, predicate, object }, i) => ({ subject, object }));
  const newMyDistrictInfo = myDistrict.map(({ subject, object }) => {
    const dbpediaLink = store.any(
      sym(subject.value),
      OWL('#sameAs'),
      null
    );
    return {
      districtName: unescape(object.value),
      dbpediaLink: dbpediaLink?.value,
    };
  });

  console.log(newMyDistrictInfo);

  const fetcher = new Fetcher(store);
  const pinus = sym('http://dbpedia.org/resource/Centro_(Madrid)');
  const profile = pinus.doc();

  // lamada asinncorona que se llama solo al crear el componente
  useEffect(() => {
    fetcher.load(profile).then(
      (response) => {
        const root = htmlParser(response.responseText);
        // buscamos los links dentro de los metadatos.
        const matched = root
          .querySelectorAll('head link')
          .filter((el) => el.getAttribute('type') === 'application/json');

        const jsonLink = matched[0].getAttribute('href');

        // request del archivo
        fetch(jsonLink)
          .then((response) => response.json())
          .then((data) => {
            // jsonParser(data, 'http://dbpedia.org/data', store);

            // metemos el archivo en nuestra store
            jsonParserFixed(data, 'http://dbpedia.org/data', store);

            // cuando lo hemos recibido cambiamos el estado a notLoading
            setloading(false);
          }); // pass base URI);
      },
      (err) => {}
    );
  }, []);

  // machear la store entera y pintarla
  const myStore = store
    .match(null, null, null, null)
    .map(({ subject, predicate, object }, i) => (
      <p key={i}>
        {subject.value} {predicate.value} {object.value}
      </p>
    ));

  return (
    <div>
      <h3>ID: {districtId}</h3>
    </div>
  );
}
