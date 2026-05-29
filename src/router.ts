/* import express, { Request, Response } from "express";
const router = express.Router();

router.get("/", (req: Request, res: Response) => {
  res.send("Home Page");
});

router.get("/login", (req: Request, res: Response) => {
  res.send("Login Page");
});

router.get("/signup", (req: Request, res: Response) => {
  res.send("Signup Page");
});

export default router;
 */

import express from "express";
const router = express.Router();
import memberController from "./controllers/member.controller";

/* router.get("/", memberController.goHome);

router.get("/login", memberController.getLogin);

router.get("/signup", memberController.getSignup); */

export default router;
