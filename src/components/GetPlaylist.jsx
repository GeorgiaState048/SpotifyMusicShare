import React, { useState, useEffect } from "react";
import axios from 'axios';

const GetPlaylists = () => {
  const [token, setToken] = useState("");
  const [data, setData] = useState({});
  useEffect(() => {
    console.log('This is the localStorage test', localStorage.getItem('access_token'));
    if (localStorage.getItem('access_token')) {
      setToken(localStorage.getItem('access_token'));
      console.log('This is a token', token);
    }
  }, []);
  const handleGetPlaylist = () => {
    console.log('This is the second print statement for token ', token);
    axios
      .get('https://api.spotify.com/v1/me/playlists', {
        headers: {
          Authorization: 'Bearer ' + token,
        },
      })
      .then((response) => {
        setData(JSON.parse(JSON.stringify(response.data)));
        console.log(data);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return <button onClick={handleGetPlaylist}>Grab Playlists</button>;
};
export default GetPlaylists;
