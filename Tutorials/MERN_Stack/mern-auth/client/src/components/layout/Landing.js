import React, { Component } from "react";
import { Link } from "react-router-dom";

class Landing extends Component {
  render(){
    return(
      <div style={{height:"75vh"}} className="container valign-wrapper">
        <div className="row">
          <div className="col s12 center-align">
            <h4>
              Bem vindo ao <b>LEARNING LOOP BRASIL</b>  {" "}
              
            </h4>
            <p className="flow-text grey-text text-darken-1">
               Aqui você encontra dicas de programação para iniciantes

            </p>
            <br/>
            <div className="col s6">
              <Link 
                to="/register"
                style={{
                  width: "140px",
                  borderRadius: "3px",
                  letterSpacing: "1.5px"
                }}
                className="btn btn-large waves-effect waves-light 
                hoverable blue accent-3"
              >
                Cadastrar
              </Link>
            </div>
            <div className="col s6">
                <Link
                  to="/login"
                  style={{
                    width: "140px",
                    borderRadius: "3px",
                    letterSpacing: "1.5px"
                  }}
                  className="btn btn-large btn-flat waves-effect white 
                  black-text"
                >
                Login
               </Link> 
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Landing;