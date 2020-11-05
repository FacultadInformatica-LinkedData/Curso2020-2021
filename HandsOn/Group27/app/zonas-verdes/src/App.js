import React, { useEffect, useState } from 'react';

import './App.css';

import CircularProgress from '@material-ui/core/CircularProgress';
import Home from './pages/Home';
import District from './pages/District';
import NoMatch from './pages/NoMatch';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import tripletas from './triplets/output-with-links.nt';
import { graph, Namespace, parse, sym, IndexedFormula } from 'rdflib';

export const ThemeContext = React.createContext(false);

function App() {
  const [store, setstore] = useState(false);

  // solo  queremos que se añadan la primera vez
  useEffect(() => {
    fetch(tripletas)
      .then((r) => r.text())
      .then((text) => {
        const newStore = graph();
        console.log(typeof text);
        parse(
          text,
          newStore,
          'http://api.zonasVerdesMadrid.com',
          'text/n3',
          () => {
            setstore(newStore);
          }
        );
      });
  }, []);

  console.log(store);

  const setMystore = (t,base,type) => {
    console.log(typeof store);
    console.log(t);
    parse(t, store, base, type, () => {
      console.log('setted');
      setstore(store);
      // setstore(newStore);
    });
  };

  return (
    <ThemeContext.Provider value={[store, setMystore]}>
      <Router>
        <div className='App'>
          {store ? (
            <Switch>
              <Route exact path='/'>
                <Home />
              </Route>
              <Route path='/District/:districtId'>
                <District />
              </Route>
              <Route path='*'>
                <NoMatch />
              </Route>
            </Switch>
          ) : (
            <CircularProgress color='inherit' />
          )}
        </div>
      </Router>
    </ThemeContext.Provider>
  );
}

export default App;
