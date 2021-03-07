import React from "react"
import MyTaste from "./MyTaste.js"
function MyInfo() {
  return (
    <div>
      <h1>Bob Ziroll</h1>
      <p>This is a paragraph about me...</p>
      <ul>
        <li>Thailand</li>
        <li>Japan</li>
        <li>Nordic Countries</li>
      </ul>
      <MyTaste/>
    </div>
  )
}

export default MyInfo;