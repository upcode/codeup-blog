title: Front-End Questions Part I
subtitle: HTML Interview Questions
name: UP[code]
date: 2016-18-1
summary: 

<h1>HTML Questions:</h1>

<h3>1. What does a doctype do?</h3>
<p>The <code>doctype</code> declaration is not an HTML tag; it is an instruction to the web browser about what version of the markup language the page is written in</p>
<p>The term DOCTYPE tells the browser which type of HTML is used on a webpage. In turn, the browsers use DOCTYPE to determine how to render a page. Failing to use DOCTYPE or using a wrong DOCTYPE may load your page in Quirks Mode.</p>

<h3>2. What's the difference between standards mode and quirks mode?</h3>
<p><code>quirk mode</code>If the browser decides that the document is old-school, it’ll render it in quirks mode. This mode applies CSS in the quirky way that suited predecessors of that browser, or even of other browsers. </p>
<p><code>standard</code>If the browser decides that the document is modern, it’ll render it in standards mode. This means that, as a rule, CSS is applied in accordance with the CSS2 specification.</p>

<h3>3. What's the difference between HTML and XHTML?</h3>
<p></p>

<h3>4. What are the differences between div and span?
</h3>
<p><code>div</code> is a block element and <code>span</code> is inline element.</p>
<p>**It is illegal to put block element inside inline element.</p> 
<p>**<code>div</code> can have a p tag and a p tag can have a span. However, span can't have a div or p tag inside.</p>

<h3>5. How do you serve a page with content in multiple languages?</h3>
<p>How do you serve a page with content in multiple languages? The first thing to get right when working with multiple languages on a website is making sure the language is identified in the code of the page.</p>

<h3>6. What kind of things must you be wary of when design or developing for multilingual sites? </h3>
<p>setting the default language, using Unicode encoding, using the ‘lang’ attribute, being aware of standard font sizes and text direction, and language word length (may affect layout).</p>


<h3>7. How do you serve a page with content in multiple languages?</h3>
<p>lang tag in the header</p>
<h3>8. What are data- attributes good for?</h3>
<p> allow you to store extra information/ data in the DOM. u can write valid html with embedded private data. You can easily access data attribute by using javascript and hence a lot of libraries like knockout uses it.</p>
<h3>9. Consider HTML5 as an open web platform. What are the building blocks of HTML5?</h3>
<ul>
<li>more semantic text markup</li> 
<li>new form elements</li>
<li>vedio and audio</li>
<li>new javascript API</li>
<li>canvas and SVG</li>
<li>new communication API</li> 
<li>geolocation API</li>
<li>web worker API</li>
<li>new data storage</li>
</ul>

<h3>10. Describe the difference between a <code>cookie</code>, <code>sessionStorage</code> and <code>localStorage.</code>?</h3>

<p><code>Cookies</code> are small text files that websites place in a browser for tracking or login purposes. localStorage</p>
<p><code>sessionStorage</code> are new objects, both of which are storage specifications but vary in scope and duration.</p>


<p><code>localStorage</code>is permanent and website-specific whereas sessionStorage only lasts as long as the duration of the longest open tab.</p>








<p></p>
<h3>11. Describe the difference between <code>script</code>, <code>script async</code> and <code>script defer</code>.?</h3>

<p><code>script async</code> used for javascript
async script executes at the first opportunity after it is finished downloading and before the window's load event. This means it's possible (and likely) that async scripts are not executed in the order in which they occur in the page.</p>
<code>script defer</code> used in safari -- scripts download immediamly without pausing the aprser
defer scripts, on the other hand, are guaranteed to be executed in the order they occur in the page. That execution starts after parsing is completely finished, but before the document's DOM ContentLoaded event.</p>

<h3>12. Why is it generally a good idea to position CSS <code>link</code>s tags in the <code>head</code> and JS <code>scripts tags</code> just before <code>body</code>? Do you know any exceptions?</h3>

<p>A <code>link</code> tag can occur only in the head element; however, there can be multiple occurrences of <code>link</code>.

In just about every case, it's best to place all your script references at the end of the page, just before <code>body</code>.

If you are unable to do so due to templating issues and whatnot, decorate your script tags with the defer attribute so that the browser knows to download your scripts after the HTML has been downloaded:
</p>

<h3>13. What is progressive rendering?</h3>
<p>dont wait for back-end data immediately render template and its content ie ajax</p>


<h3>14. Can you explain the differnce between GET and POST?</h3>

They are two types of HTTP requests <code>GET</code> and <code>POST</code>
<p><code>GET</code> use url the send data. AJAX <code>GET</code> in IE will be cached, so to ensure data updates, beter add a timestamp</p>
<p><code>POST</code> represent actions on resources, like insert/update/delete. They usually sent from HTML form. Lareg data could be sent by <code>POST</code>. Data is send along with HTTP header, instead of data of GET in the URL</p>


 <h3>15. What is semantic HTML?</h3>
 <p> allow you to store extra information/ data in the DOM. u can write valid html with embedded private data. You can easily access data attribute by using javascript and hence a lot of libraries like knockout uses it.</p>
 <h3>16. When should you use <code>section</code>, <code>div</code> or <code>article</code></h3>
 <p>
 	<code>section</code>, group of content inside is related to a single theme, and should appear as an entry in an outline of the page. It’s a chunk of related content, like a subsection of a long article, a major part of the page (eg the news section on the homepage), or a page in a webapp’s tabbed interface. A section normally has a heading (title) and maybe a footer too.</p>
<p><code>article</code>, represents a complete, or self-contained, composition in a document, page, application, or site and that is, in principle, independently distributable or reusable, e.g. in syndication. This could be a forum post, a magazine or newspaper article, a blog entry, a user-submitted comment, an interactive widget or gadget, or any other independent item of content.</p>
<p><code>div</code>, on the other hand, does not convey any meaning, aside from any found in its class, lang and title attributes.</p>

<h3>17. What is HTML?</h3>
<p>HTML stands for HyperText Markup Language. It is the dominant markup language for creating websites and anything that can be viewed in a web browser</p>
<h3>18. What is the difference between HTML elements and tags?</h3>
<p>HTML elements communicate to the browser how to render text. When surrounded by angular brackets <> they form HTML tags. For the most part, tags come in pairs and surround text.</p>
<h3>19. What are the limitations when serving XHTML pages?</h3>
<p>Perhaps the biggest issue is the poor browser support XHTML currently enjoys. Internet Explorer and a number of other user agents cannot parse XHTML as XML. Thus, it is not the extensible language it was promised to be.</p>

<h3>20.  What is the difference between linking to an image, a website, and an email address?</h3>
<p>To link an image, use <code>img</code> tags. You need specify the image in quotes using the source attribute, <code>src</code>
in the opening tag.</p> 
<p> For hyperlinking, the anchor tag, <code>a</code>, is used and the link is specified in the <code>href</code>attribute. Text to be hyperlinked should be placed between the anchor tags. Little known fact: href stands for “hypertext reference.” When linking to an email, the href specification will be</p>





