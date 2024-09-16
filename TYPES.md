<div class="w3-col l10 m12" id="main">

<h1>Python <span class="color_h1">Data Types</span></h1>
<div class="w3-clear nextprev">
<a class="w3-left w3-btn" href="python_variables_exercises.asp">❮ Previous</a>
<a class="w3-right w3-btn" href="python_numbers.asp">Next ❯</a>
</div>
<hr>

<h2>Built-in Data Types</h2>
<p>In programming, data type is an important concept.</p>
<p>Variables can store data of different types, and different types can do 
different things.</p>
<p>Python has the following data types built-in by default, in these categories:</p>
<table class="w3-table">
  <tbody><tr>
    <td style="width:160px;">Text Type:</td>
    <td><code class="w3-codespan">str</code></td>
  </tr>
  <tr>
    <td>Numeric Types:</td>
    <td><code class="w3-codespan">int</code>, <code class="w3-codespan">float</code>,
    <code class="w3-codespan">complex</code></td>
  </tr>
  <tr>
    <td>Sequence Types:</td>
    <td><code class="w3-codespan">list</code>, <code class="w3-codespan">tuple</code>, 
    <code class="w3-codespan">range</code></td>
  </tr>
  <tr>
    <td>Mapping Type:</td>
    <td><code class="w3-codespan">dict</code></td>
  </tr>
  <tr>
    <td>Set Types:</td>
    <td><code class="w3-codespan">set</code>, <code class="w3-codespan">frozenset</code></td>
  </tr>
  <tr>
    <td>Boolean Type:</td>
    <td><code class="w3-codespan">bool</code></td>
  </tr>
  <tr>
    <td>Binary Types:</td>
    <td><code class="w3-codespan">bytes</code>, <code class="w3-codespan">bytearray</code>, 
    <code class="w3-codespan">memoryview</code></td>
  </tr>
  <tr>
    <td>None Type:</td>
    <td><code class="w3-codespan">NoneType</code></td>
  </tr>
</tbody></table>

<hr>
<h2>Getting the Data Type</h2>

<p>You can get the data type of any object by using the <code class="w3-codespan">type()</code> function:</p>

<div class="w3-example">
<h3>Example<a class="ws-black ws-hover-black spaces-tryit ga-featured" href="/python/python_server.asp" title="W3Schools Spaces" target="_blank">Get your own Python Server</a></h3>
  <p>Print the data type of the variable x:</p>
<div class="w3-code notranslate pythonHigh"><span class="pythoncolor" style="color:black">
x = <span class="pythonnumbercolor" style="color:red">5</span><br>
<span class="pythonkeywordcolor" style="color:mediumblue">print</span>(<span class="pythonkeywordcolor" style="color:mediumblue">type</span>(x))<span class="pythonnumbercolor" style="color:red">
</span> </span></div>
<a target="_blank" class="w3-btn w3-margin-bottom" href="trypython.asp?filename=demo_type">Try it Yourself »</a>
</div>

<hr>

<h2>Setting the Data Type</h2>

<p>In Python, the data type is set when you assign a value to a variable:</p>
<style>
#dtref td:nth-child(1) {
  font-family: Consolas,"courier new";
  font-size: 110%;
}
</style>
<table id="dtref" class="ws-table-all notranslate">
<tbody><tr>
<th style="min-width:350px">Example</th>
<th>Data Type</th>
<th style="width:90px">Try it</th>
</tr>
<tr>
<td>x = "Hello World"</td>
<td>str</td>
<td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_type_str">Try it »</a></td>
</tr>
<tr>
<td>x = 20</td>
<td>int</td>
<td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_type_int">Try it »</a></td>
</tr>
<tr>
<td>x = 20.5</td>
<td>float</td>
<td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_type_float">Try it »</a></td>
</tr>
<tr>
<td>x = 1j</td>
<td>complex</td>
<td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_type_complex">Try it »</a></td>
</tr>
<tr>
<td>x = ["apple", "banana", "cherry"]</td>
<td>list</td>
<td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_type_list">Try it »</a></td>
</tr>
  <tr>
<td>x = ("apple", "banana", "cherry")</td>
<td>tuple</td>
<td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_type_tuple">Try it »</a></td>
  </tr>
  <tr>
<td>x = range(6)</td>
<td>range</td>
<td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_type_range">Try it »</a></td>
  </tr>
  <tr>
<td>x = {"name" : "John", "age" : 36}</td>
<td>dict</td>
<td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_type_dict">Try it »</a></td>
  </tr>
  <tr>
<td>x = {"apple", "banana", "cherry"}</td>
<td>set</td>
<td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_type_set">Try it »</a></td>
  </tr>
  <tr>
<td>x = frozenset({"apple", "banana", "cherry"})</td>
<td>frozenset</td>
<td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_type_frozenset">Try it »</a></td>
  </tr>
  <tr>
<td>x = True</td>
<td>bool</td>
<td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_type_bool">Try it »</a></td>
  </tr>
  <tr>
<td>x = b"Hello"</td>
<td>bytes</td>
<td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_type_bytes">Try it »</a></td>
  </tr>
  <tr>
<td>x = bytearray(5)</td>
<td>bytearray</td>
<td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_type_bytearray">Try it »</a></td>
  </tr>
<tr>
<td>x = memoryview(bytes(5))</td>
<td>memoryview</td>
<td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_type_memoryview">Try it »</a></td>
</tr>
<tr>
<td>x = None</td>
<td>NoneType</td>
<td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_type_nonetype">Try it »</a></td>
</tr>
</tbody></table>

<hr>
<div id="midcontentadcontainer" style="overflow:auto;text-align:center">
<!-- MidContent -->
<!-- <p class="adtext">Advertisement</p> -->

  <div id="adngin-mid_content-0" style="min-width: 728px; min-height: 280px; display: flex; justify-content: space-around; align-items: center; width: 728px; flex-direction: row;"><div id="adngin-mid_content-0-adaptive-group-2-placement-0" data-google-query-id="COTdw7Xe74cDFeG0ywEdS7oB3A"><div id="sn_ad_label_adngin-mid_content-0-adaptive-group-2-placement-0" class="sn_ad_label" style="color:#000000;font-size:12px;margin:0;text-align:center;">ADVERTISEMENT</div><div id="google_ads_iframe_/22152718,16833175/sws-hb//w3schools.com//mid_content_1__container__" style="border: 0pt;"><iframe id="google_ads_iframe_/22152718,16833175/sws-hb//w3schools.com//mid_content_1" name="google_ads_iframe_/22152718,16833175/sws-hb//w3schools.com//mid_content_1" title="3rd party ad content" width="1" height="1" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" aria-label="Advertisement" tabindex="0" data-load-complete="true" data-google-container-id="7" style="border: 0px; vertical-align: bottom; width: 300px; height: 250px;"></iframe></div></div><div id="adngin-mid_content-0-adaptive-group-2-placement-1" data-google-query-id="CLrVxbXe74cDFeG0ywEdS7oB3A"><div id="sn_ad_label_adngin-mid_content-0-adaptive-group-2-placement-1" class="sn_ad_label" style="color:#000000;font-size:12px;margin:0;text-align:center;">ADVERTISEMENT</div><div id="google_ads_iframe_/22152718,16833175/sws-hb//w3schools.com//mid_content_0__container__" style="border: 0pt; display: inline-block; width: 300px; height: 250px;"><iframe frameborder="0" src="https://34174c463bc75ab15bee19769ad04240.safeframe.googlesyndication.com/safeframe/1-0-40/html/container.html" id="google_ads_iframe_/22152718,16833175/sws-hb//w3schools.com//mid_content_0" title="3rd party ad content" name="" scrolling="no" marginwidth="0" marginheight="0" width="300" height="250" data-is-safeframe="true" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" aria-label="Advertisement" tabindex="0" data-google-container-id="8" style="border: 0px; vertical-align: bottom;" data-load-complete="true"></iframe></div></div></div>
  
</div>
<hr>

<h2>Setting the Specific Data Type</h2>
<p>If you want to specify the data type, you can use the following 
constructor functions:</p>

<table id="dtref" class="ws-table-all notranslate">
<tbody><tr>
<th style="min-width:350px">Example</th>
<th>Data Type</th>
<th style="width:90px">Try it</th>
</tr>
<tr>
<td>x = str("Hello World")</td>
<td>str</td>
<td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_type_str2">Try it »</a></td>
</tr>
<tr>
<td>x = int(20)</td>
<td>int</td>
<td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_type_int2">Try it »</a></td>
</tr>
<tr>
<td>x = float(20.5)</td>
<td>float</td>
<td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_type_float2">Try it »</a></td>
</tr>
<tr>
<td>x = complex(1j)</td>
<td>complex</td>
<td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_type_complex2">Try it »</a></td>
</tr>
<tr>
<td>x = list(("apple", "banana", "cherry"))</td>
<td>list</td>
<td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_type_list2">Try it »</a></td>
</tr>
  <tr>
<td>x = tuple(("apple", "banana", "cherry"))</td>
<td>tuple</td>
<td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_type_tuple2">Try it »</a></td>
  </tr>
  <tr>
<td>x = range(6)</td>
<td>range</td>
<td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_type_range2">Try it »</a></td>
  </tr>
  <tr>
<td>x = dict(name="John", age=36)</td>
<td>dict</td>
<td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_type_dict2">Try it »</a></td>
  </tr>
  <tr>
<td>x = set(("apple", "banana", "cherry"))</td>
<td>set</td>
<td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_type_set2">Try it »</a></td>
  </tr>
  <tr>
<td>x = frozenset(("apple", "banana", "cherry"))</td>
<td>frozenset</td>
<td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_type_frozenset2">Try it »</a></td>
  </tr>
  <tr>
<td>x = bool(5)</td>
<td>bool</td>
<td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_type_bool2">Try it »</a></td>
  </tr>
  <tr>
<td>x = bytes(5)</td>
<td>bytes</td>
<td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_type_bytes2">Try it »</a></td>
  </tr>
  <tr>
<td>x = bytearray(5)</td>
<td>bytearray</td>
<td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_type_bytearray2">Try it »</a></td>
  </tr>
<tr>
<td>x = memoryview(bytes(5))</td>
<td>memoryview</td>
<td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_type_memoryview2">Try it »</a></td>
</tr>
</tbody></table>

<a id="exercises"></a>
<hr>
<form autocomplete="off" id="w3-exerciseform" action="exercise.asp?filename=exercise_datatypes1" method="post" target="_blank">
<h2>Test Yourself With Exercises</h2>
<div class="exercisewindow">
<h2>Exercise:</h2>
<p>The following code example would print the data type of x, what data type would that be?</p>
<div class="exerciseprecontainer">
<pre>x = 5
print(type(x))
<input name="ex1" maxlength="3" style="width: 35px;">
</pre>
</div>
<br>
<button type="submit" class="w3-btn w3-margin-bottom">Submit Answer »</button>
<p><a target="_blank" href="exercise.asp?filename=exercise_datatypes1">Start the Exercise</a></p>
</div>
</form>

<br>
<div class="w3-clear nextprev">
<a class="w3-left w3-btn" href="python_variables_exercises.asp">❮ Previous</a>
<a class="w3-right w3-btn" href="python_numbers.asp">Next ❯</a>
</div>
<div id="user-profile-bottom-wrapper" class="user-profile-bottom-wrapper">
  <div class="user-authenticated w3-hide">
    <a href="https://profile.w3schools.com/log-in?redirect_url=https%3A%2F%2Fwww.w3schools.com%2Fpython%2Fpython_datatypes.asp" class="user-profile-btn ga-bottom ga-bottom-profile" title="Your W3Schools Profile" aria-label="Your W3Schools Profile" target="_top">
      <svg xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 2048 2048" class="user-profile-icon" aria-label="Your W3Schools Profile Icon">
        <path d="M 843.500 1148.155 C 837.450 1148.515, 823.050 1149.334, 811.500 1149.975 C 742.799 1153.788, 704.251 1162.996, 635.391 1192.044 C 517.544 1241.756, 398.992 1352.262, 337.200 1470 C 251.831 1632.658, 253.457 1816.879, 340.500 1843.982 C 351.574 1847.431, 1696.426 1847.431, 1707.500 1843.982 C 1794.543 1816.879, 1796.169 1632.658, 1710.800 1470 C 1649.008 1352.262, 1530.456 1241.756, 1412.609 1192.044 C 1344.588 1163.350, 1305.224 1153.854, 1238.500 1150.039 C 1190.330 1147.286, 1196.307 1147.328, 1097 1149.035 C 1039.984 1150.015, 1010.205 1150.008, 950 1149.003 C 851.731 1147.362, 856.213 1147.398, 843.500 1148.155" stroke="none" fill="#2a93fb" fill-rule="evenodd"></path>
        <path d="M 1008 194.584 C 1006.075 194.809, 999.325 195.476, 993 196.064 C 927.768 202.134, 845.423 233.043, 786 273.762 C 691.987 338.184, 622.881 442.165, 601.082 552 C 588.496 615.414, 592.917 705.245, 611.329 760.230 C 643.220 855.469, 694.977 930.136, 763.195 979.321 C 810.333 1013.308, 839.747 1026.645, 913.697 1047.562 C 1010.275 1074.879, 1108.934 1065.290, 1221 1017.694 C 1259.787 1001.221, 1307.818 965.858, 1339.852 930.191 C 1460.375 795.998, 1488.781 609.032, 1412.581 451.500 C 1350.098 322.327, 1240.457 235.724, 1097.500 202.624 C 1072.356 196.802, 1025.206 192.566, 1008 194.584" stroke="none" fill="#0aaa8a" fill-rule="evenodd"></path>
      </svg>

      <svg xmlns="http://www.w3.org/2000/svg" class="user-progress" aria-label="Your W3Schools Profile Progress">
        <path class="user-progress-circle1" fill="none" d="M 25.99650934151373 15.00000030461742 A 20 20 0 1 0 26 15"></path>
        <path class="user-progress-circle2" fill="none" d="M 26 15 A 20 20 0 0 0 26 15"></path>
      </svg>

      <span class="user-progress-star">★</span>

      <span class="user-progress-point">+1</span>
    </a>
  </div>

  <div class="w3s-pathfinder -teaser user-anonymous">
  <div class="-background-image -variant-t2">&nbsp;</div>

  <div class="-inner-wrapper">
    <div class="-main-section">
      <div class="-inner-wrapper">
        <div class="-title">W3schools Pathfinder</div>

        <div class="-headline">Track your progress - it's free!</div>
      
        <div class="-body">
          <div class="-progress-bar">
            <div class="-slider" style="width: 20%;">&nbsp;</div>    
          </div>
        </div>
      </div>
    </div>

    <div class="-right-side-section">
      <div class="-user-session-btns">
        <a href="https://profile.w3schools.com/log-in?redirect_url=https%3A%2F%2Fpathfinder.w3schools.com&amp;origin=https%3A%2F%2Fwww.w3schools.com%2Fpython%2Fpython_datatypes.asp" class="-login-btn w3-btn bar-item-hover w3-right ws-light-green ga-bottom ga-bottom-login" title="Login to your account" aria-label="Login to your account" target="_top">
          Log in
        </a>

        <a href="https://profile.w3schools.com/sign-up?redirect_url=https%3A%2F%2Fpathfinder.w3schools.com&amp;origin=https%3A%2F%2Fwww.w3schools.com%2Fpython%2Fpython_datatypes.asp" class="-signup-btn w3-button w3-right ws-green ws-hover-green ga-bottom ga-bottom-signup" title="Sign Up to Improve Your Learning Experience" aria-label="Sign Up to Improve Your Learning Experience" target="_top">
          Sign Up
        </a>
      </div>
    </div>
  </div>
</div>

</div>

</div>