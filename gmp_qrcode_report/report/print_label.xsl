<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" 
xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
xmlns:fo="http://www.w3.org/1999/XSL/Format"> 
	<!--<xsl:variable name="initial_bottom_pos">19.5</xsl:variable>
	<xsl:variable name="initial_left_pos">0.35</xsl:variable>
	<xsl:variable name="height_increment">11.5</xsl:variable>
	<xsl:variable name="width_increment">10.2</xsl:variable>
	<xsl:variable name="frame_height">12.0cm</xsl:variable>
	<xsl:variable name="frame_width">10.20cm</xsl:variable>
	<xsl:variable name="number_columns">2</xsl:variable>
	<xsl:variable name="max_frames">6</xsl:variable>--> 
	<xsl:variable name="initial_bottom_pos">19.5</xsl:variable>
	<xsl:variable name="initial_left_pos">0.35</xsl:variable>
	<xsl:variable name="height_increment">9.0</xsl:variable>
	<xsl:variable name="width_increment">10.2</xsl:variable>
	<xsl:variable name="frame_height">9.5cm</xsl:variable>
	<xsl:variable name="frame_width">10.16cm</xsl:variable>
	<xsl:variable name="number_columns">2</xsl:variable>
	<xsl:variable name="max_frames">6</xsl:variable> 
		
	<xsl:template match="/">
		<xsl:apply-templates select="lots"/>
	</xsl:template>  

	<xsl:template match="lots">
		<document>
			<template leftMargin="2.0cm" rightMargin="2.0cm" topMargin="2.0cm" bottomMargin="2.0cm" title="Address list" author="Generated by Open ERP">
			<pageTemplate id="all">
					<pageGraphics/>
					<xsl:apply-templates select="lot-line" mode="frames"/> 
			</pageTemplate> 
			</template>  
			<stylesheet>
				<paraStyle name="nospace" fontName="Courier" fontSize="10" spaceBefore="0" spaceAfter="0"/>
				
 
    <blockTableStyle id="Standard_Outline">
      <blockAlignment value="LEFT"/>
      <blockValign value="TOP"/>
    </blockTableStyle>  
    <blockTableStyle id="Table1">
          <blockTopPadding value="0"/>
      <blockBottomPadding value="0"/>
	  
      	
      <blockAlignment value="CENTER"/>
      <blockValign value="TOP"/>
      <lineStyle kind="LINEBEFORE" colorName="#000000" start="0,0" stop="0,-1"/>
      <lineStyle kind="LINEABOVE"  colorName="#000000" start="0,0" stop="0,0"/>
      <lineStyle kind="LINEBELOW"  colorName="#000000" start="0,-1" stop="0,-1"/>
      <lineStyle kind="LINEBEFORE" colorName="#000000" start="1,0" stop="1,-1"/>
      <lineStyle kind="LINEABOVE"  colorName="#000000" start="1,0" stop="1,0"/>
      <lineStyle kind="LINEBELOW"  colorName="#000000" start="1,-1" stop="1,-1"/>
      <lineStyle kind="LINEBEFORE" colorName="#000000" start="2,0" stop="2,-1"/>
      <lineStyle kind="LINEAFTER"  colorName="#000000" start="2,0" stop="2,-1"/>
      <lineStyle kind="LINEABOVE"  colorName="#000000" start="2,0" stop="2,0"/>
      <lineStyle kind="LINEBELOW"  colorName="#000000" start="2,-1" stop="2,-1"/>
    </blockTableStyle>
      <blockTableStyle id="Table2">
	  	<blockAlignment value="LEFT"/>
      	<blockValign value="TOP"/>
	  </blockTableStyle>
      <blockTableStyle id="Table21">
		<blockAlignment value="LEFT"/>
      	<blockValign value="TOP"/>
	  </blockTableStyle>
      <blockTableStyle id="Table3">
		<blockAlignment value="LEFT"/>
      	<blockValign value="TOP"/>
	  </blockTableStyle>
      <blockTableStyle id="Table31">
		<blockAlignment value="LEFT"/>
      	<blockValign value="TOP"/>
	  </blockTableStyle>
      <blockTableStyle id="Table4">
		<blockAlignment value="LEFT"/>
      	<blockValign value="TOP"/>
	  </blockTableStyle>
    <initialize>
      <paraStyle name="all" alignment="justify"/>
    </initialize>
	<paraStyle name="P1" rightIndent="6.0" leftIndent="6.0" fontName="Helvetica" fontSize="6.5" leading="11" alignment="CENTER"/>
	<paraStyle name="P2" rightIndent="6.0" leftIndent="6.0" fontName="Helvetica" fontSize="8.5" leading="13" alignment="LEFT"/>
    <paraStyle name="P3" rightIndent="6.0" leftIndent="6.0" fontName="Helvetica" fontSize="6.5" leading="11" alignment="LEFT"/>
    <paraStyle name="P4" rightIndent="0.0" leftIndent="2.0" fontName="Helvetica" fontSize="8.0" leading="12" alignment="LEFT"/>
    <paraStyle name="P6" rightIndent="6.0" leftIndent="6.0" fontName="Helvetica" fontSize="9.5" leading="13" alignment="RIGHT"/>
    <paraStyle name="P7" rightIndent="6.0" leftIndent="6.0" fontName="Helvetica" fontSize="7.5" leading="11" alignment="RIGHT"/>
    <paraStyle name="P8" rightIndent="6.0" leftIndent="6.0" fontName="Helvetica" fontSize="8.5" leading="12" alignment="RIGHT"/>
	<paraStyle name="P44" rightIndent="6.0" leftIndent="6.0" fontName="Helvetica" fontSize="12.0" leading="12" alignment="CENTER"/>
	<paraStyle name="P45" rightIndent="6.0" leftIndent="6.0" fontName="Helvetica" fontSize="10.5" leading="12" alignment="CENTER"/>
	<paraStyle name="P46" rightIndent="6.0" leftIndent="6.0" fontName="Helvetica" fontSize="9.5" leading="8" alignment="CENTER"/>
	<paraStyle name="P47" rightIndent="6.0" leftIndent="6.0" fontName="Helvetica" fontSize="9.5" leading="11" alignment="LEFT"/>
	<paraStyle name="P48" rightIndent="6.0" leftIndent="6.0" fontName="Helvetica" fontSize="9.5" leading="11" alignment="CENTER"/>
	<paraStyle name="P25" rightIndent="6.0" leftIndent="6.0" fontName="Helvetica" fontSize="8.5" leading="9" alignment="RIGHT"/>
    <paraStyle name="Standard" fontName="Helvetica" fontSize="11.5" leading="15"/>
    <paraStyle name="Text body" fontName="Helvetica" fontSize="11.5" leading="15" spaceBefore="0.0" spaceAfter="6.0"/>
    <paraStyle name="List" fontName="Helvetica" fontSize="11.5" leading="15" spaceBefore="0.0" spaceAfter="6.0"/>
    <paraStyle name="Table Contents" fontName="Helvetica" fontSize="11.5" leading="15" spaceBefore="0.0" spaceAfter="6.0"/>
    <paraStyle name="Table Heading" fontName="Helvetica-BoldOblique" fontSize="11.5" leading="15" alignment="CENTER" spaceBefore="0.0" spaceAfter="6.0"/>
    <paraStyle name="Caption" fontName="Helvetica-Oblique" fontSize="9.5" leading="14" spaceBefore="6.0" spaceAfter="6.0"/>
    <paraStyle name="Index" fontName="Helvetica" fontSize="11.5" leading="15"/>
    <images/>
		</stylesheet>
		<story>
				<xsl:apply-templates select="lot-line" mode="story"/>
			</story>
		</document>
	</xsl:template>
	 <xsl:template match="lot-line" mode="frames">
		<xsl:if test="position() &lt; $max_frames + 1"> 
			<frame>
				<xsl:attribute name="width">
					<xsl:value-of select="$frame_width"/> 
				</xsl:attribute>
				<xsl:attribute name="height">
					<xsl:value-of select="$frame_height"/>
				</xsl:attribute>  
				<xsl:attribute name="x1">
					<xsl:value-of select="$initial_left_pos + ((position()-1) mod $number_columns) * $width_increment"/>
					<xsl:text>cm</xsl:text> 
				</xsl:attribute>
				<xsl:attribute name="y1">
					<xsl:value-of select="$initial_bottom_pos - floor((position()-1) div $number_columns) * $height_increment"/>
					<xsl:text>cm</xsl:text> 
				</xsl:attribute> 				
			</frame>
		</xsl:if> 
	</xsl:template>  
	
	<xsl:template match="lot-line" mode="story">
	<!--<blockTable colWidths="384.0" rowHeights="319.68" style="Table1">-->
	<blockTable colWidths="270.0" rowHeights="255.0" style="Table1">
      
		<tr>
        <td>
        <blockTable colWidths="270.0" style="Table21">        
        <!--<blockTable colWidths="384.0" style="Table21">-->	
	    	<tr>
        		<para style="Table Contents">
        		</para>        		
        	</tr>	
        	<tr>
		        <td>
		       	 	<para style="P44"><b>Name: </b><xsl:value-of select="name"/></para>
		        </td>
	        </tr>	          
	        <tr>
		        <td>
		        	<para style="P44"><b>Serial No: </b><xsl:value-of select="serial"/></para>
		        </td>
	        </tr>
	        <tr>
		        <td>
		        	<para style="P44"><b>Qty: </b><xsl:value-of select="qty"/></para>
		        </td>
	        </tr>
	        <tr>
		        <td>
		        	<para style="P44"><b>Destination: </b><xsl:value-of select="dest"/></para>
		        </td>
	        </tr>
	        <tr>
		        <td>
		        	<para style="P44"><b>Source Doc: </b><xsl:value-of select="origin"/></para>
		        </td>
	        </tr>
	        <tr>
		        <td>
		        	<para style="P44"><b>Date: </b><xsl:value-of select="date"/></para>
		        </td>
	        </tr>  
        </blockTable> 
        <para style="Table Contents">
        </para>   
             	        
      	<xsl:if test="qr">        	
        	<barCode code="qrcode" x="1cm" y="1cm" height="3cm" ><xsl:value-of select="qr"/></barCode> 
      	</xsl:if>
      	      
       </td>      </tr>
    </blockTable>	
    <nextFrame/>	
	</xsl:template>
</xsl:stylesheet>