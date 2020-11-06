import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import IconButton from '@material-ui/core/IconButton';
import Typography from '@material-ui/core/Typography';
import InfoIcon from '@material-ui/icons/Info';
import EcoIcon from '@material-ui/icons/Eco';

import { Link } from 'react-router-dom';

const useStyles = makeStyles({
  root: {
    minWidth: 275,
  },
  bullet: {
    display: 'inline-block',
    margin: '0 2px',
    transform: 'scale(0.8)',
  },
  title: {
    fontSize: 14,
  },
  pos: {
    marginBottom: 12,
  },
});

export default function SimpleCard({ districtname, totalspecies }) {
  const classes = useStyles();
  const number = totalspecies ? (
    <span>
      {' '}
      {totalspecies} <EcoIcon htmlColor='#026e00' />
    </span>
  ) : (
    <span>
      {' '}
      ? <EcoIcon htmlColor='#026e00' />
    </span>
  );

  return (
    <Card className={classes.root}>
      <CardContent>
        <Typography
          className={classes.title}
          color='textSecondary'
          gutterBottom
        >
          {districtname}
        </Typography>
        <Typography variant='h5' component='h2'>
          {number}
        </Typography>
      </CardContent>
      <CardActions>
        <Link to={`/District/${districtname}`}>
          <IconButton>
            <InfoIcon />
          </IconButton>
        </Link>
      </CardActions>
    </Card>
  );
}
