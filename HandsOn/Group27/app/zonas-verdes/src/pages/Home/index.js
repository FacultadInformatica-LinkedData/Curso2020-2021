import React, { useEffect, useState, useContext } from 'react';
import SpacingGrid from '../../components/SpacingGrid';
import CircularProgress from '@material-ui/core/CircularProgress';
import { ThemeContext } from "../../App";

import {
  Namespace,
  sym,
} from 'rdflib';

export default function Home() {
  const [store, setMystore] = useContext(ThemeContext);
  // creamos una store
  const [loading, setLoading] = useState(true);
  const [allDistrictsInfo, setsAllDistrictsInfo] = useState([]);

  // crear nameSpaces
  const ONT = new Namespace('http://api.zonasVerdesMadrid.com/ontologies/');

  // solo  queremos que se añadan la primera vez
  useEffect(() => {
        const allDistricts = store
          .match(null, ONT('districts#hasName'), null)
          .map(({ subject, predicate, object }, i) => ({ subject, object }));
        const newAllDistrictsInfo = allDistricts.map(({ subject, object }) => {
          const totalSpecies = store.any(
            sym(subject.value),
            ONT('districts#hasTotal'),
            null
          );
          return {
            districtName: unescape(object.value),
            totalSpecies: totalSpecies?.value,
          };
        });
        setsAllDistrictsInfo(newAllDistrictsInfo);
  }, [store]);



  useEffect(() => {
    setLoading(false);
  }, [allDistrictsInfo]);




  return (
    <div>
      <h1>Zonas verdes de Madrid</h1>
      {loading ? (
        <CircularProgress color='inherit' />
      ) : (
        <SpacingGrid data={allDistrictsInfo}></SpacingGrid>
      )}
    </div>
  );
}
