import express from "express";
import path from "path";
import router from "./router";
import routerAdmin from "./router-admin";
import morgan from "morgan";
import { MORGAN_FORMAT } from "./libs/config";

/** 1–ENTRANCE **/
const app = express();
app.use(express.static(path.join(__dirname, "public"))); //MIDDLEWARE DP: public folderni ochadi
app.use(express.urlencoded({ extended: true })); //MIDDLEWARE DP: Traditional API
app.use(express.json()); //MIDDLEWARE DP: REST API
app.use(morgan(MORGAN_FORMAT)); //MIDDLEWARE DP:

/** 2–SESSIONS **/

/** 3–VIEWS **/
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "ejs");

/** 4–ROUTERS **/
app.use("/admin", routerAdmin); // SSR
app.use("/", router); // SPA
// //Middleware Design Pattern

export default app;

//bssr
