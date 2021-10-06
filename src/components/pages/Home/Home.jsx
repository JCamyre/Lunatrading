import React from "react";
import { Grid, Typography } from "@material-ui/core";
// import HeroSection from '../HeroSection.js';
// import Cards from '../Cards.js';
// import Chart from '../Chart';
// import Parallax from '../Parallax';
// import bg_img from '../../images/bg-img-1.jpg';
import SearchBar from "../../SearchBar/SearchBar";

export default function Home() {
  const background_image = require("../../../images/bg-img-3.jpg").default;
  const background_image2 = require("../../../images/bg-img-1.jpg").default;

  return (
    <div>
      <Grid container spacing={1}>
        {/* Good video for a drop down menu: https://www.youtube.com/watch?v=IF6k0uZuypA */}
        <Grid
          item
          align="center"
          style={{ margin: "auto", zIndex: 0, position: "relative" }}
        >
          <div
            style={{
              backgroundImage: "url(" + background_image + ")",
              backgroundSize: "auto",
              boxShadow:
                "0 16px 24px 2px rgb(0 0 0 / 14%), 0 6px 30px 5px rgb(0 0 0 / 12%), 0 8px 10px -5px rgb(0 0 0 / 20%)",
              width: "1903px",
              height: "750px",
              padding: "0px 35px 0px 35px",
              position: "relative",
              filter: "brightness(90%)",
            }}
          >
            <Grid
              item
              xs={12}
              align="flex-start"
              style={{
                filter: "brightness(100%)",
                position: "relative",
                left: "-500px",
                top: "345px",
              }}
            >
              <SearchBar />
            </Grid>
          </div>
        </Grid>

        <Grid
          item
          xs={12}
          align="center"
          style={{ padding: "0px 75px", zIndex: 1, alignItems: "center" }}
        >
          <div
            className="container"
            style={{
              marginRight: "350px",
              width: "1400px",
              fontWeight: "300px",
              fontFamily: ["Roboto", "Helvetica"],
              padding: "40px 60px",
              lineHeight: "1.5em",
              borderRadius: "6px",
              boxShadow:
                "0 16px 24px 2px rgb(0 0 0 / 14%), 0 6px 30px 5px rgb(0 0 0 / 12%), 0 8px 10px -5px rgb(0 0 0 / 20%)",
            }}
          >
            <Grid item xs={12} align="center">
              <h3>
                Lunatrading is a website aimed at traders who want to take their research and due diligence to the next level. <br/> Our countless features will ensure you are well informed for your next trade.
              </h3>
            </Grid>
            <Grid item xs={12} align="center">
              <img
                style={{ height: "auto", width: "50%", borderRadius: "6px", padding: "0 0" }}
                alt="nasdaq sign"
                src={background_image2}
              />
            </Grid>
          </div>
        </Grid>
        {/* <Grid item xs={12} align='center'>
                    <CustomCarousel />
                </Grid> */}
      </Grid>
    </div>
  );
}
