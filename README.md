# Project_I

# Introduction

### Brief Overview:
- Ever heard stories about shark attacks in movies or on the news? Some of these tales can be pretty scary, right? Well, we're on a mission to find out the real story behind shark attacks. By looking at lots of information collected over the years, we want to find out which sharks are most often involved in these incidents. Are some sharks friendlier than others? Do sharks prefer munching on surfboards or flippers? Let's dive in and discover the truth about our finned friends in the ocean!

### Where Did We Get Our Information?:
- We found a cool collection of facts and details all about shark attacks. It's like a giant shark diary that anyone can read! If you're curious and want to see it for yourself, check it out [here](https://www.kaggle.com/datasets/teajay/global-shark-attacks).

### Words to Know:
- Fatal (Y/N): Tells us if someone was seriously hurt during a shark encounter. Y means "yes, it was serious," and N means "nope, they were okay."
- Case Number: It's like a special code for each shark story.
- cleaned_species: This is just a fancy name we use for the type of shark, like "Great White" or "Hammerhead."
- Age Group: This tells us how old someone was when they met a shark, like if they were a kid, a teenager, or a grown-up.

# Questions to be answered
### Primary Questions: 

- Which shark species are most frequently involved in attacks?
- Which are the top 10 shark species with the highest number of recorded attacks?
### Secondary Questions:
 - For the top 10 sharks, how many attacks were fatal versus not fatal?
 - How many shark attacks on surfers and paddleboarders were fatal versus non-fatal?
 - How do the outcomes of shark attacks vary by age group for surfers and paddleboarders?
# Cleaning
### Observations:
- Dataset columns have missing values.
- Several columns exhibit data inconsistencies.
- Some columns seem redundant for analysis.
### Methods & Tools Used:
- Libraries: numpy, pandas, matplotlib, seaborn.
- Cleaning Techniques:
- Removal of empty rows.
- Corrections in Case Number (e.g., removing "xx" and "0").
- Transformation of Year values from formats like '2000.0' to '2000'.
- Standardization of date formats.
- Parsing and cleaning of various age formats.
### Challenges Faced:
- Misspellings: Correcting entries like 'Boatomg' to 'Boating'.
- Missing Values: Filling in missing Case Number using data from another column.
- Complex Age Data: Handling age ranges like '20-25', words such as 'Teen', and combinations.
- Date Formats: Standardizing various date patterns to a consistent format.

# Transforming
### Objective:
- We transformed our shark data to make it neat and consistent, ensuring our analysis is smooth and accurate.

### Methods & Tools Used:
- Standardization: Unified the naming of shark species for consistency.
- Age Grouping: Categorized people into groups like 'Children', 'Teenagers', and 'Adults'.
- Date Formatting: Ensured all dates are written in the same style.
- Handling Missing Data: Made decisions on how to address gaps in our data.
### Outcome:
- After the transformation, our data is cleaner and more organized. With consistent shark names, uniform date styles, and clear age categories, our dataset is now ready for deeper analysis.
# Visualization
- Visualizing our data helps turn complex information into easy-to-understand graphics. Below are the visual results for our five main questions:

### Which shark species are most frequently involved in attacks?
![Count of Shark Species](./images/Shark%20Species/Count_Sharkspecies2.png)
### Which are the top 10 shark species with the highest number of recorded attacks?
![Count of Top 10 Shark Species](./images/Shark%20Species/Count_Sharkspecies_top10_bar.png)
![Pie Chart of Top 10 Shark Species](./images/Shark%20Species/top10_Sharkspecies_pie.png)


### For the top 10 sharks, how many attacks were fatal versus not fatal?
![Fatality by Top 10 Shark Species](./images/Shark%20Species/top10_Sharkspecies_fatality_bar.png)

### How many shark attacks on surfers and paddleboarders were fatal versus non-fatal?
![Fatality in Surf vs Paddle](./images/Surf%20v%20paddle/fatality_surf_vs_paddle.png)

### How do the outcomes of shark attacks vary by age group for surfers and paddleboarders?
![Fatality in Surf vs Paddle by Ages](./images/Surf%20v%20paddle/fatality_surf_vs_paddle_ages.png)

# Conclusion

### Alright, ocean adventurers, here's the splashy scoop on our sharky friends:

#### The Usual Suspects: If there was a "Shark's Got Talent" show... 
- The White Shark would steal the limelight with 667 show-stopping appearances
### 
- Following behind, we have the Bull Shark with its 283 encores
- The Blacktip Shark with 103
- The Nurse Shark with 97
- All vying for the title of "Top Predator" out of 1,600 oceanic showdowns.
- On a Scale of 1 to Fatal: Despite their Hollywood reputation, sharks aren't as keen on turning every encounter into a thriller
- Only a third of the time do things get, well, bitey-bitey
- For many of our finned stars, it's more about the chase than the chomp

### Who Tastes Better?

- Surfers are like the fast-food of the ocean to sharks, with only a 6.5% chance of getting a nibble, meaning 78 out of 1,219 got a bit more than they bargained for.
- Paddleboarders, on the other hand, are like a three-course meal, with a whopping 33.4% ending in a fin-tastic disaster. That's 115 gourmet experiences out of 344.
- Diving Deeper: While 4,301 of our ocean tales end on a positive note, 1,389 take a darker twist. And for 612 stories, well, the ending is still being written.

### Key Insights:
- Sharks may have a rep as the "bad boys" of the ocean, but most of the time, they're just cruising for a snack—not a smackdown. Whether you're hanging ten or paddling out, remember: the ocean is their turf, and it's all in good fin! 🦈🌊