# testing beautiful soup with teststand

from bs4 import BeautifulSoup

tshelp = '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=ISO-8859-1">
<META NAME="Microsoft.Help.Id" CONTENT="TestStand_TSHelp_TSHelp.html" />
<meta name="Microsoft.Help.TocParent" content="-1" />
<meta name="Microsoft.Help.TocOrder" content="0" />
<script src="../APILink.js" type="text/javascript"></script>
<script src="../UILink.js" type="text/javascript"></script>
<script src="../RefLink.js" type="text/javascript"></script>
<script src="../TSSyncServer.js" type="text/javascript"></script>

<script src="../TSDeployLink.js" type="text/javascript"></script>
<script src="../TSHelpLink.js" type="text/javascript"></script>
<script src="../pdf.js" type="text/javascript"></script>
<script src="../web.js" type="text/javascript"></script>

<script src="../TSErrors.js" type="text/javascript"></script>
<script src="../TSExamples.js" type="text/javascript"></script>
<script src="../TSExampleLaunch.js" type="text/javascript"></script>
<script src="../TSLabVIEW.js" type="text/javascript"></script>
<script src="../TSReports.js" type="text/javascript"></script>
<script src="../feedbacklink.js" type="text/javascript"></script>
<link rel="STYLESHEET" type="text/css" href="minimal.css">
<link rel="STYLESHEET" type="text/css" href="TestStand.css">
<title>TestStand 2019 Help</title>
</head>

<body bgcolor="#ffffff">
<div id="browserContent">

<p class="Anchor"><img src="../Art/nieagle.gif"></p>

<h1>TestStand 2019 Help</h1>

<p class="Body">May 2019, 370052AA-01
</p>

<p class="Body">Use this help file to complete the following tasks:</p>

<ul>
	<li>Understand TestStand <a href="tsfundamentals.chm::/InfoTopics/TSFundamentals.html">concepts</a>, including creating and debugging sequences, <a href="tsfundamentals.chm::/InfoTopics/Database_Connectivity.htm">logging data</a> and <a href="tsreports.chm::/InfoTopics/TSReports.htm">generating and customizing reports</a>, customizing TestStand functionality, and integrating TestStand with other application development environments, such as <a href="tslabview.chm::/InfoTopics/TSLabVIEW.htm">LabVIEW</a> and LabWindows/CVI.</li>
	<li>Explore the TestStand <a href="tsref.chm::/InfoTopics/TestStand_Ref.htm">environment</a>.</li>
	<li>Browse the <!-- $h3m$href="ms-xhelp:///?method=page&id=TestStand_TSUIRef_TestStand_UI.htm&product=vs&productversion=100" --><a href="tsuiref.chm::/InfoTopics/TestStand_UI.htm">TestStand User Interface Controls</a> and <!-- $h3m$href="ms-xhelp:///?method=page&id=TestStand_TSAPIRef_TestStand_API.html&product=vs&productversion=100" --><a href="tsapiref.chm::/InfoTopics/TestStand_API.html">TestStand Engine</a> APIs, and learn how to use the <!-- $h3m$href="ms-xhelp:///?method=page&id=TestStand_TSAPIRef_ActiveX_Automation_Overview.html&product=vs&productversion=100" --><a href="tsapiref.chm::/InfoTopics/ActiveX_Automation_Overview.html">TestStand ActiveX Automation server</a>.</li>
	<li>Learn how to <a href="tsdeploysystem.chm::/InfoTopics/TSDUDefault.htm">deploy TestStand systems</a>.</li>
	<li>Review the <a href="tsexamples.chm::/InfoTopics/Examples.htm">example test programs</a>, including sequence files, code modules, and other supporting files.</li>
</ul>

<table class="Borderless">
	<tr>
		<td class="Icon"><img src="../Art/note.gif"></td>
		<td><strong>Note</strong>&nbsp;&nbsp;If you open help files directly from the <span class="Monospace"><a href="tsfundamentals.chm::/InfoTopics/Directories.html">&lt;TestStand&gt;</a>\Doc\Help</span> directory, National Instruments recommends that you open <span class="Monospace">TSHelp.chm</span> first because this file is a collection of all the TestStand help files and provides a complete table of contents and index.</td>
	</tr>
</table>
<p class="Body">
Refer to the following topics for more information about this help file:
</p>

<p class="Body"><a href="../NITopics/Glossary.html">Glossary</a></p>
<p class="Body"><a href="../NITopics/Technical_Support_Resources.html">NI Services</a></p>
<p>To comment on National Instruments documentation, refer to the <a href="javascript:WWW(WWW_Feedback)">National Instruments website</a>.</p>


<table class="Borderless">
<tr>
<td class="Icon"><img src="../Art/note.gif" alt="Note"></td>
<td><strong>Note</strong>&nbsp;&nbsp;Use Microsoft Internet Explorer version 8 or later to ensure the online help prints properly.</td>
</tr>
</table>
<p class="Body">
&#0169; 2000&#8211;2019 National Instruments. All rights reserved.</p>
<p class="Body">Refer to the <span class="Monospace">&lt;National Instruments&gt;\_Legal Information</span> directory for information about NI copyright,  patents, trademarks, warranties, product warnings, and export compliance.</p>

</div>
</body>
</html>
'''

soup = BeautifulSoup(tshelp, features="html.parser")

for title_text in soup.find_all('title'):
	print(title_text.get_text())

for h1_text in soup.find_all('h1'):
	print(h1_text.get_text())
