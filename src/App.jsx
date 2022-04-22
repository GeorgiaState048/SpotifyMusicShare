/* eslint-disable linebreak-style */
/* eslint-disable react/button-has-type */
/* eslint-disable react/jsx-one-expression-per-line */
/* eslint-disable no-param-reassign */
/* eslint-disable camelcase */
/* eslint-disable prefer-template */
/* eslint-disable no-unused-vars */
/* eslint-disable no-trailing-spaces */

import './App.css';
import {
  useEffect, useState, React,
} from 'react';
import env from 'react-dotenv';
import Logo from './images/logo.jpg';
import { Playlists } from './Info';

// import axios from 'axios'
// import UserProfile from './components/UserProfile';

const SPOTIFY_KEY = env.CLIENT_ID; // insert your client id here from spotify
const SPOTIFY_AUTHORIZE_ENDPOINT = 'https://accounts.spotify.com/authorize';
const USER_ENDPOINT = 'https://api.spotify.com/v1/me';
const REDIRECT_URL_AFTER_LOGIN = 'https://whispering-sierra-18640.herokuapp.com/ ';
const SPACE_DELIMITER = '%20';
const SCOPES = [
  'user-read-currently-playing',
  'user-read-playback-state',
];
const SCOPES_URL_PARAM = SCOPES.join(SPACE_DELIMITER);
console.log(SPOTIFY_KEY);

const getReturnedParamsFromSpotifyAuth = (hash) => {
  const stringAfterHashtag = hash.substring(1);
  const paramsInUrl = stringAfterHashtag.split('&');
  const paramsSplitUp = paramsInUrl.reduce((accumulater, currentValue) => {
    const [key, value] = currentValue.split('=');
    accumulater[key] = value;
    return accumulater;
  }, {});
  return paramsSplitUp;
};

function App() {
  const [data, setData] = useState({});
  const [token, setToken] = useState('');
  const [name, setName] = useState('');
  const [image, setImage] = useState('');
  const [playlists, setPlaylists] = useState([]);

  useEffect(() => {
    if (window.location.hash) {
      const {
        access_token,
        // expiresIn,
        // tokenType,
      } = getReturnedParamsFromSpotifyAuth(window.location.hash);
      localStorage.clear();

      localStorage.setItem('access_token', access_token);
      setToken(access_token);
      const newData = { token };
      console.log(newData);
      fetch('/get_access_token', {
        method: 'POST',
        headers: { 'Content-type': 'application/json' },
        body: JSON.stringify(newData),
      });
    }
  });

  function handleLogin() {
    window.location = `${SPOTIFY_AUTHORIZE_ENDPOINT}?client_id=${SPOTIFY_KEY}&redirect_uri=${REDIRECT_URL_AFTER_LOGIN}&scope=${SCOPES_URL_PARAM}&response_type=token&show_dialog=true`;
  }

  // the json file returns a list of playlist names
  function renderPlaylistNames(i) {
    return (
      <body> 
        <a href={playlists[i][1]}>{playlists[i][0]}</a>
      </body>
    );
  }

  // when the get playlists button is clicked, it accesses the API endpoint
  // i created in the get_playlists() in app.py and gets the playlist info
  // from that function
  const handleGetUserPlaylists = () => {
    const getData = async () => {
      const response = await fetch('/get_playlists');
      const info = await response.json();
      console.log(info);
      const pl_names = info[0];
      setPlaylists(pl_names.PlaylistNames);
    };
    getData();
  };

  // when the get user info button is clicked, it accesses the API endpoint
  // i created in the get_user_info() in app.py and gets the user info
  // from that function
  const handleGetUserProfile = () => {
    const getData = async () => {
      const response = await fetch('/user_info');
      const info = await response.json();
      console.log(info);
      const username = info[0];
      const pic = info[1];
      setName(username.Username);
      setImage(pic.ProfilePic);
    };
    getData();
  };

  // I use map function to print each playlist
  const myPlaylists = playlists.map((currElement, index) => (
    <p className="rowC">
      {renderPlaylistNames(index)}
    </p>
  ));

  const link = '/home'; // link to go back to the previous page
  return (
    <div className="container">
      <body>
        <h1>SPOTIFY MUSIC SHARE</h1>
        <div className="topleft">
          <img src={Logo} alt="Logo" width="140" height="125" />
        </div>
        <div>
          <h1>
            After you login, you must press the Get User Info and Get User Playlists buttons!
          </h1>
        </div>
        <button className="btn" onClick={handleLogin}>log in to spotify</button>
        <button className="btn" onClick={handleLogin}>Switch Users</button>
        <button className="btn" onClick={handleGetUserProfile}>Get User Info</button>
        <button className="btn" onClick={handleGetUserPlaylists}>Get User Playlists</button>
        <a href={link}>Go To The HomePage!</a>
        {name}
        <div className="Profle">
          <img src={image} alt="Profile Pic" width="250" height="300" />
          {myPlaylists}
        </div>
      </body>
    </div>
  );
}

export default App;
