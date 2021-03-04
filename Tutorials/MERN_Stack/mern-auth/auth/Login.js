import React, { Component } from "react";
import { Link } from "react-router-dom";

class Login extends Component {
  constructor(){
    super();
    this.state = {
      email: "",
      password:"",
      errors: {}
    };
  }

  onChange = e =>{
    this.setState({ [e.target.id ]: e.target.value });
  };

  onSubmit = e => {
    e.preventDefault();

    const userData = {
      email: this.state.email,
      password: this.state.password
    };

    console.log(userData);
  };

}