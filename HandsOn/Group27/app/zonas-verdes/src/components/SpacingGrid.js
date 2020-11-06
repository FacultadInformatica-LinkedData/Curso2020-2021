import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import SimpleCard from './SimpleCard';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  simpleCard: {
    height: 140,
    width: 100,
  },
  control: {
    padding: theme.spacing(2),
  },
}));

export default function SpacingGrid({data}) {
  // console.log(data);
  const classes = useStyles();
  return (
    <Grid container className={classes.root} spacing={2}>
      <Grid item xs={12}>
        <Grid container justify="center" spacing={2}>
          {data.map(({districtName, totalSpecies}) => (
            <Grid key={districtName} item>
              <SimpleCard className={classes.simpleCard} districtname={districtName}  totalspecies={totalSpecies}/>
            </Grid>
          ))}
        </Grid>
      </Grid>
    </Grid>
  );
}
