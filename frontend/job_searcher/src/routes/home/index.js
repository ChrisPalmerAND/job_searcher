import style from "./style.css";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import { FormControl, FormLabel } from "@mui/material";
import Box from "@mui/material/Box";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import Select, { SelectChangeEvent } from "@mui/material/Select";
import * as React from "react";
import { spacing } from "@mui/system";

const Home = () => {
  const [age, setAge] = React.useState("");

  const handleChange = (event) => {
    setAge(event.target.value);
  };

  return (
    <>
      <h1>Welcome to the job searcher</h1>

      <form action="http://127.0.0.1:8000/jobs" method="post">
        <FormControl fullWidth>
          <InputLabel id="whichWebsite">Website</InputLabel>
          <Select
            labelId="whichWebsiteLabel"
            id="whichWebsiteSelect"
            value={age}
            label="Website"
            onChange={handleChange}
            name="website"
          >
            <MenuItem value={1}>LinkedIn</MenuItem>
            <MenuItem value={2} disabled>
              Google - coming soon
            </MenuItem>
            <MenuItem value={3} disabled>
              Indeed - coming soon
            </MenuItem>
          </Select>
          <TextField
            id="keywordsInput"
            name="keywords"
            label="Keywords"
            sx={{ mt: 3 }}
          />

          <TextField
            id="locationInput"
            name="location"
            label="Location"
            sx={{ mt: 3 }}
          />

          <Button variant="contained" type="submit" sx={{ mt: 3 }}>
            Search
          </Button>
        </FormControl>
      </form>
    </>
  );
};

export default Home;
