title: Front-End Questions Part II
subtitle: CSS Interview Questions
name: UP[code]
date: 2016-18-1
summary: 

<h1>CSS Questions:</h1>


<h3>1. What is the difference between classes and ID's in CSS?</h3>
Id’s are unique
● Each element can have only one ID
● Each page can have only one element with that ID
­­your code will not pass validation if you use the same ID on more than one element. Classes are NOT unique
● You can use the same class on multiple elements.
● You can use multiple classes on the same element.
­­Any styling information that needs to be applied to multiple objects on a page should be done with a class
­­Can you give an example?
­­id are unique apply to on attribute
­­class apply to multiple attributes with same class name

<h3>2. What's the difference between "resetting" and "normalizing" CSS? Which would you choose, and why?</h3>
CSS resets removes all built­in browser styling. Standard elements like H1­6, p, strong, em, etc end up looking exactly alike, having no decoration at all.
­­You're then supposed to add all decoration yourself.
Normalize CSS a ims to make built­in browser styling consistent across browsers. Elements like H1­6 will appear bold, larger et cetera in a consistent way across browsers.
­­ You're then supposed to add only the difference in decoration your design needs.

<h3>3. Describe Floats and how they work.</h3>











<h3>4. Describe z­index and how stacking context is formed.</h3>
<h3>5. Describe BFC(Block Formatting Context) and how it works.</h3>
<h3>6. What are the various clearing techniques and which is appropriate for what context?</h3>
<h3>7. Explain CSS sprites, and how you would implement them on a page or site.</h3>
<h3>8. What are your favourite image replacement techniques and which do you use when?</h3>
<h3>9. How would you approach fixing browser­specific styling issues?</h3>
<h3>10. How do you serve your pages for feature­constrained browsers?</h3>
<h3>a. What techniques/processes do you use?</h3>



























<h3>11. What are the different ways to visually hide content (and make it available only for screen readers)?</h3>
<h3>12. Have you ever used a grid system, and if so, what do you prefer?</h3>
<h3>13. Have you used or implemented media queries or mobile specific layouts/CSS?</h3>
<h3>14. Are you familiar with styling SVG?</h3>
<h3>15. How do you optimize your webpages for print?</h3>
<h3>16. What are some of the "gotchas" for writing efficient CSS?</h3>
<h3>17. What are the advantages/disadvantages of using CSS preprocessors?</h3>
a. Describe what you like and dislike about the CSS preprocessors you have used.
CSS Questions</h3>
 <h3>18. How would you implement a web design comp that uses non­standard fonts?</h3>
<h3>19. Explain how a browser determines what elements match a CSS selector</h3>
<h3>20. Describe pseudo­elements and discuss what they are used for.</h3>
<h3>21. Explain your understanding of the box model and how you would tell the browser in CSS to render your layout in different box models.</h3>
<h3>22. What does * { box­sizing: border­box; } do? What are its advantages?</h3>
<h3>23. List as many values for the display property that you can remember.</h3>
<h3>24. What's the difference between inline and inline­block?</h3>
<h3>25. What's the difference between a relative, fixed, absolute and statically positioned element?</h3>
<h3>26. The 'C' in CSS stands for Cascading. How is priority determined in assigning styles (a few examples)? How can you use this system to your advantage?</h3>
<h3>27. What existing CSS frameworks have you used locally, or in production? How would you change/improve them?</h3>
<h3>28. Have you played around with the new CSS Flexbox or Grid specs?</h3>
<h3>29. How is responsive design different from adaptive design?</h3>
<h3>30. Have you ever worked with retina graphics? If so, when and what techniques did you use?</h3>
<h3>31. Is there any reason you'd want to use translate() instead of absolute positioning, or vice­versa? And why?</h3>




CSS Specificity Rules
● If two selectors apply to the same element, the one with higher specificity wins.
● Specificity determines, which CSS rule is applied by the browsers.
● Specificity is usually the reason why your CSS­rules don’t apply to some elements,
although you think they should.
● Every selector has its place in the specificity hierarchy.
● If two selectors apply to the same element, the one with higher specificity wins.
● There are four distinct categories which define the specificity level of a given selector:
inline styles, IDs, classes+attributes and elements.
● You can understand specificity if you love Star Wars: C SS Specificity Wars. 
● You can understand specificity if you love poker: C SS Specificity for Poker Players
● When selectors have an equal specificity value, the latest rule is the one that counts.
● When selectors have an unequal specificity value, the more specific rule is the one that
counts.
● Rules with more specific selectors have a greater specificity.
● The last rule defined overrides any previous, conflicting rules.
● The embedded style sheet has a greater specificity than other rules.
● ID selectors have a higher specificity than attribute selectors.
● You should always try to use IDs to increase the specificity.
● A class selector beats any number of element selectors.
● The universal selector and inherited selectors have a specificity of 0, 0, 0, 0.
● You can calculate CSS specificity with CSS Specificity Calculator.