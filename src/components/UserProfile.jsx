/* eslint-disable linebreak-style */
/* eslint-disable react/button-has-type */
/* eslint-disable react/function-component-definition */
/* eslint-disable prefer-template */
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const USER_ENDPOINT = 'https://api.spotify.com/v1/me';

const UserProfile = () => {
  const [token, setToken] = useState('');
  const [data, setData] = useState({});
  const [username, setUsername] = useState('');
  const [image, setImage] = useState('');

  console.log('This is the localStorage test', localStorage.getItem('access_token'));

  useEffect(() => {
    console.log('This is the localStorage test', localStorage.getItem('access_token'));
    if (localStorage.getItem('access_token')) {
      setToken(localStorage.getItem('access_token'));
      console.log('This is a token', token);
      const newData = { token };
      fetch('/user_info', {
        method: 'POST',
        headers: { 'Content-type': 'application/json' },
        body: JSON.stringify(newData),
      });
    }
  }, []);
  useEffect(() => {
    const getData = async () => {
      const response = await fetch('/user_info');
      const info = await response.json();
      console.log(info);
      const name = data[0];
      const pic = data[1];
      setUsername(name.Username);
      setImage(pic.ProfilePic);
    };
    getData();
  }, []);
  const handleGetUserProfile = () => {
    console.log('This is the second print statement for token ', token);
    axios
      .get(USER_ENDPOINT, {
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

  return (
    <body>
      <div>
        <button onClick={handleGetUserProfile}>Get User Info</button>
        {username}
        {image}
      </div>
    </body>
  );
};

export default UserProfile;
