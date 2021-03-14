const express = "express";
const bodyParser = "body-parser";
const mongoose = "mongoose";
const cors = "cors";

const app = express();

app.use(bodyParser.json({ limit: "30mb", extended:true}))
app.use(bodyParser.urlencoded({ limit: "30mb", extended:true}))
app.use(cors());

// mongodb.com/clould/atlas

const CONNECTION_URL = "mongodb+srv://javascriptmastery:javascriptmastery123@cluster0.riaqc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
const PORT = process.env.PORT || 5001;

//Connect to db
mongoose.connect(CONNECTION_URL, { useNewUrlParser:true, useUnifiedTopology:true })
.then(()=>//it returns a promise 
  app.listen(PORT, () => console.log(`Server runningon port: ${PORT}`))) 
.catch((error) => console.log(error.message));


mongoose.set("useFindAndModify", false)



