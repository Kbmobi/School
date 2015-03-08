<!--
Lab Number: 8
Program Name if applicable: Lab8
Author name and email addres: Keegan Bailey, kbailey.v@gmail.com
Date of submission: 3/2/2013
Time estimated to complete the lab: 6 hours
Actual time taken to complete the lab: 8 hours
A description of the program: Use MVC to make SQL querys
required to run the program if applicable: controller.php, model.php, toXML.php, view.xsl, sq_connect.inc
-->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
 <xsl:template match="/">
  <html>
   <body>
	<h1>
		<xsl:value-of select="root/title"/>
	</h1>
	<h2>
		<xsl:value-of select="root/Input/title"/>
	</h2>
	<form method="post" action="controller.php">
		<ul>
			<xsl:for-each select="root/Input/entry">
				<li>
					<xsl:value-of select="name"/>
					<input type="text" name="input[]" value="{value}"/>
				</li>
			</xsl:for-each>
		</ul>
		<input type="submit"/>
	</form>
	<h2>
		<xsl:value-of select="root/Output/title"/>
	</h2>
	<table border="1">
		<xsl:for-each select="root/Output/entry">
			<tr>
				<xsl:for-each select="value">
					<td>
						<xsl:value-of select="."/>
					</td>
				</xsl:for-each>
			</tr>
		</xsl:for-each>
	</table>
   </body>
  </html>
 </xsl:template>
</xsl:stylesheet>