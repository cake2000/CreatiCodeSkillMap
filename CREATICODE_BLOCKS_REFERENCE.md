# CreatiCode Blocks Reference for T15 Skills Verification

This document extracts all blocks from `/media/binyu/USB2/ScratchCopilot/blockdes8.txt` in the following categories:
1. Looks
2. Widgets
3. AI Speech/Text-to-Speech

This reference is needed to verify that T15 skills accurately reflect CreatiCode features.

---

## LOOKS CATEGORY

### Display Control

#### looks_show
- **Syntax:** `show`
- **Usage Example:** `show`
- **Description:** For 2D, make the sprite visible on the stage. For 3D, make the sprite object (current selected 3D object created from this sprite) visible in the 3D scene.
- **Can be used for 3D:** true

#### looks_hide
- **Syntax:** `hide`
- **Usage Example:** `hide`
- **Description:** For 2D, make the sprite invisible on the stage. For 3D, make the sprite object (current selected 3D object created from this sprite) invisible in the 3D scene.
- **Can be used for 3D:** true

### Speech and Thought Bubbles

#### looks_sayforsecs_withstyle
- **Block ID:** looks_sayforsecs_withstyle
- **Syntax:** `say [TEXT] for (T) seconds text size (FONTSIZE) [FONTCOLOR] background [BACKGROUNDCOLOR] edge [EDGECOLOR]`
- **Usage Example:** `say [Hi] for (3) seconds text size (16) [#FFFFFFFF] background [#000000FF] edge [#FFFFFFFF]`
- **Description:** Show the given TEXT as wrapped in a speech bubble. The text can be styled with a FONTSIZE, FONTCOLOR, BACKGROUNDCOLOR and EDGECOLOR. This block provides more styling compared to the original 'say' block from standard Scratch blocks. If the number of seconds T is not empty or 0, the speech bubble will disappear after T seconds automatically, otherwise the speech bubble will remain visible.
- **Can be used for 3D:** false

#### looks_thinkforsecs_withstyle
- **Block ID:** looks_thinkforsecs_withstyle
- **Syntax:** `think [TEXT] for (T) seconds text size (FONTSIZE) [FONTCOLOR] background [BACKGROUNDCOLOR] edge [EDGECOLOR]`
- **Usage Example:** `think [Oh] for (3) seconds text size (16) [#FFFFFFFF] background [#000000FF] edge [#FFFFFFFF]`
- **Description:** Show the given TEXT as wrapped in a thought bubble. The text can be styled with a FONTSIZE, FONTCOLOR, BACKGROUNDCOLOR and EDGECOLOR. This block provides more styling compared to the original 'think' block from standard Scratch blocks. If the number of seconds T is not empty or 0, the thought bubble will disappear after T seconds automatically, otherwise the thought bubble will remain visible.
- **Can be used for 3D:** false

### Size Control

#### looks_setsizeto
- **Block ID:** looks_setsizeto
- **Syntax:** `set size to (N) %`
- **Usage Example:** `set size to (100) %`
- **Description:** For 2D projects, set the sprite's size to the given percentage, where 'size' is the scale percentage. E.g. size of 150 means 150% of the original costume size. For 3D projects, change the scale percentage by N for the 'sprite object' (the selected 3D object that's created within this sprite). For example, if size is set to 120, then the sprite object's scale becomes 120% in all 3 dimensions.
- **Can be used for 3D:** true

#### looks_size
- **Block ID:** looks_size
- **Syntax:** `(size)`
- **Usage Example:** `(size)`
- **Description:** For 2D block, a reporter block that returns the sprite's current size scale as a percentage. For 3D projects, this reporter block returns the current scale of the 'sprite object' (the selected 3D object created from the current sprite).
- **Can be used for 3D:** true

#### looks_changesizeby
- **Block ID:** looks_changesizeby
- **Syntax:** `change size by (N)`
- **Usage Example:** `change size by (10)`
- **Description:** For 2D projects, change the sprite's size by N, where 'size' is the scale percentage. E.g. size of 150 means 150% of the original costume size. For 3D projects, change the scale percentage by N for the 'sprite object' (the selected 3D object that's created within this sprite). For example, if size changes from 110 to 120, then the sprite object's scale changes from 110% to 120%.
- **Can be used for 3D:** true

#### looks_reducesizeby
- **Block ID:** looks_reducesizeby
- **Syntax:** `reduce size by (N)`
- **Usage Example:** `reduce size by (10)`
- **Description:** Reduce the sprite's size by N percentage points.
- **Can be used for 3D:** true

### Visual Effects

#### looks_effectgradually
- **Block ID:** looks_effectgradually
- **Syntax:** `[ACTION v] sprite gradually in (T) seconds`
- **Usage Example:** `[fade v] sprite gradually in (1) seconds`
- **Description:** ACTION can be 'fade' or 'reveal', so this block will make the sprite fade or reveal gradually over T seconds.
- **Can be used for 3D:** false

#### looks_colour
- **Block ID:** looks_colour
- **Syntax:** `color (C) saturation (S) brightness (B) transparency (T)`
- **Usage Example:** `color (40) saturation (100) brightness (100) transparency (0)`
- **Description:** Creates a color value with specified color, saturation, brightness, and transparency parameters.
- **Can be used for 3D:** false

### Text Printing

#### looks_printtext
- **Block ID:** looks_printtext
- **Syntax:** `print [TEXT] at x (XPOS) y (YPOS) width (W) height (H) color [FONTCOLOR]`
- **Usage Example:** `print [Hi] at x (0) y (0) width (300) height (100) color [#2CADE5FF]`
- **Description:** Print text at the given x and y coordinates, and scaled up or down proportionally so that the text fits into the given window of width and height. The text can be styled with a color.
- **Can be used for 3D:** false

#### looks_printtextforsecs
- **Block ID:** looks_printtextforsecs
- **Syntax:** `print [TEXT] at x (XPOS) y (YPOS) width (W) height (H) color [FONTCOLOR] for (T) seconds`
- **Usage Example:** `print [Hi] at x (0) y (0) width (300) height (100) color [#2CADE5FF] for () seconds`
- **Description:** Print text at the given x and y coordinates, and scaled up or down proportionally so that the text fits into the given window of width and height. The text can be styled with a color. If the number of seconds is specified, the text will disappear after that many seconds. Otherwise, it will stay on the screen until the project is stopped.
- **Can be used for 3D:** false

#### looks_draw_text
- **Block ID:** looks_draw_text
- **Syntax:** `draw text [TEXT] at x (X) y (Y) size (SIZE) color (COLOR) rotation (ROTATION)`
- **Usage Example:** `draw text [hi] at x (0) y (100) size (18) color (#122829FF) rotation (0)`
- **Description:** Draw text at the given x and y positions in the given font size and font color. The text can be rorated by the given degrees clockwise. This block can be used to draw text directly on the sprite's current costume assuming it is in vector format, not draw on the stage.
- **Can be used for 3D:** false

#### looks_clearallmyprints
- **Block ID:** looks_clearallmyprints
- **Syntax:** `clear all my prints`
- **Usage Example:** `clear all my prints`
- **Description:** Clear all the text and drawing printed by this sprite using the 'print' and 'draw' blocks in the 'Looks' category. Does not affect the drawings done by the 'Pen' blocks.
- **Can be used for 3D:** false

#### looks_clearallprints
- **Block ID:** looks_clearallprints
- **Syntax:** `clear all prints`
- **Usage Example:** `clear all prints`
- **Description:** Clear all the text and drawing printed by all sprites using the 'print' and 'draw' blocks in the 'Looks' category. Does not affect the drawings done by the 'Pen' blocks.
- **Can be used for 3D:** false

### Drawing Shapes on Costumes

#### looks_draw_rectangle
- **Block ID:** looks_draw_rectangle
- **Syntax:** `draw rectangle at x (XPOS) y (YPOS) width (W) height (H) fill [FILLCOLOR] border [BORDERCOLOR] width (BORDERWIDTH) corner radius (CORNERRADIUS) rotation (N)`
- **Usage Example:** `draw rectangle at x (0) y (0) width (200) height (100) fill [#6269F8FF] border [#20B755FF] width (1) corner radius (0) rotation (90)`
- **Description:** Draw a rectangle at the given x and y position with the given width and height. The rectangle can be styled with a FILLCOLOR, BORDERCOLOR, BORDERWIDTH and CORNERRADIUS. The rectangle can be rorated by N degrees clockwise as well. This block can be used to draw a rectangle directly on the sprite's current costume assuming it is in vector format, not draw on the stage.
- **Can be used for 3D:** false

#### looks_draw_oval
- **Block ID:** looks_draw_oval
- **Syntax:** `draw oval at x (XPOS) y (YPOS) width (W) height (H) fill [FILLCOLOR] border [BORDERCOLOR] width (BORDERWIDTH) rotation (N)`
- **Usage Example:** `draw oval at x (0) y (0) width (200) height (100) fill [#E2F9F2FF] border [#F44399FF] width (1) rotation (-90)`
- **Description:** Draw an oval at the given x and y positions with the given width and height. The oval can be styled with a FILLCOLOR, BORDERCOLOR and BORDERWIDTH. The oval can be rorated by N degrees clockwise as well. This block can be used to draw an oval directly on the sprite's current costume assuming it is in vector format, not draw on the stage.
- **Can be used for 3D:** false

#### looks_draw_line
- **Block ID:** looks_draw_line
- **Syntax:** `draw line in [LINECOLOR] from x (FROMX) y (FROMY) to x (TOX) y (TOY) thickness (THICKNESS)`
- **Usage Example:** `draw line in [#386AF8FF] from x (0) y (0) to x (100) y (100) thickness (2)`
- **Description:** Draw a line between 2 points: (FROMX, FROMY) to (TOX, TOY). The line can be styled with LINECOLOR and THICKNESS. This block can be used to draw a line directly on the sprite's current costume assuming it is in vector format, not draw on the stage.
- **Can be used for 3D:** false

#### looks_draw_curve
- **Block ID:** looks_draw_curve
- **Syntax:** `draw curve in [LINECOLOR] from x (FROMX) y (FROMY) to x (TOX) y (TOY) control 1 x (CONTROLX1) y (CONTROLY1) control 2 x (CONTROLX2) y (CONTROLY2) thickness (THICKNESS)`
- **Usage Example:** `draw curve in [#05DC6DFF] from x (20) y (20) to x (200) y (20) control 1 x (20) y (100) control 2 x (200) y (100) thickness (1)`
- **Description:** Draw a bezier curve from the point (FROMX, FROMY) to the point (TOX, TOY), using two control points of (CONTROLX1, CONTROLY1) and (CONTROLX2, CONTROLY2). The curve can be styled with LINECOLOR and THICKNESS. This block can be used to draw a curve directly on the sprite's current costume assuming it is in vector format, not draw on the stage.
- **Can be used for 3D:** false

#### looks_clear_drawing
- **Block ID:** looks_clear_drawing
- **Syntax:** `clear all drawings`
- **Usage Example:** `clear all drawings`
- **Description:** Remove all drawings on this sprite's current costume, assuming it is in vector mode, and the drawings are done also using looks blocks, such as rectangle/oval/text/line/curve.
- **Can be used for 3D:** false

### Costume Management

#### looks_addcostumefromurl
- **Block ID:** looks_addcostumefromurl
- **Syntax:** `add costume named [NAME] from URL [URL] max width (W) max height (H)`
- **Usage Example:** `add costume named [car] from URL [https://carurl.png] max width (240) max height (240)`
- **Description:** Add the image from the given URL as a new costume, scale it down so it is within the given maximum width and height.
- **Can be used for 3D:** false

#### looks_addcostumefromstagesnapshot
- **Block ID:** looks_addcostumefromstagesnapshot
- **Syntax:** `add stage snapshot as costume named [NAME]`
- **Usage Example:** `add stage snapshot as costume named [c1]`
- **Description:** Takes a snapshot of the stage and save it as a costume of this sprite with the given name. This block allows the LLM to "see" the stage if we attach the costume to the chat with the LLM.
- **Can be used for 3D:** false

#### looks_exporting_costume_image
- **Block ID:** looks_exporting_costume_image
- **Syntax:** `export costume named [costume1]`
- **Usage Example:** `export costume named [costume1]`
- **Description:** Export the current costume to the user's computer. A bitmap costume will be saved as a PNG file, and a vector costume will be saved as an svg file.
- **Can be used for 3D:** false

### Stage Properties

#### looks_stage_mode
- **Block ID:** looks_stage_mode
- **Syntax:** `stage mode`
- **Usage Example:** `stage mode`
- **Description:** A reporter block for the stage mode, which can be 'Normal', 'Fullscreen' or 'Minimized'.
- **Can be used for 3D:** false

#### looks_stage_width
- **Block ID:** looks_stage_width
- **Syntax:** `stage width`
- **Usage Example:** `stage width`
- **Description:** A reporter block for the stage width, which is the actual size of the stage window in the browser window. For example, the stage width can be 240 when the 'stage mode' is 'Minimized', 480 at normal mode, and can be at 1200 at full screen level. Note that when the stage is at different size, the canvas size is still the same, but it is scaled to fit the stage window.
- **Can be used for 3D:** false

#### looks_stage_height
- **Block ID:** looks_stage_height
- **Syntax:** `stage height`
- **Usage Example:** `stage height`
- **Description:** A reporter block for the stage height, which is the actual size of the stage window in the browser window. For example, the stage height can be 180 when the 'stage mode' is 'Minimized', 360 at normal mode, and can be at 900 at full screen level.
- **Can be used for 3D:** false

#### looks_layernumber
- **Block ID:** looks_layernumber
- **Syntax:** `layer number`
- **Usage Example:** `layer number`
- **Description:** The display layer of this sprite.
- **Can be used for 3D:** false

---

## WIDGETS CATEGORY

### Text Input Widgets

#### widget_addtextbox
- **Block ID:** widget_addtextbox
- **Syntax:** `add textbox at X (X) Y (Y) width (W) height (H) padding (P) line [LINETYPE v] scroll [SCROLLTYPE v] mode [MODETYPE v] as [textbox1]`
- **Usage Example:** `add textbox at X (0) Y (0) width (200) height (30) padding (6) line [single v] scroll [scroll v] mode [input v] as [t1]`
- **Description:** Adds a textbox widget with width of W and height of H, centered at the position of (X, Y). The text inside the textbox will have a padding of P around the 4 borders. The LINETYPE can be 'single' or 'multiple', which controls whether the textbox only contain one line or multiple lines. The SCROLLTYPE can be 'scroll' or 'no scroll', which controls whether a scrollbar is shown. The MODETYPE can be 'read only' or 'input'. The last input is a name for the textbox and it can not be empty.
- **Can be used for 3D:** false

#### widget_addrichtextbox
- **Block ID:** widget_addrichtextbox
- **Syntax:** `add rich textbox at X (X) Y (Y) width (W) height (H) padding (P) mode [MODE v] as [NAME]`
- **Usage Example:** `add rich textbox at X (0) Y (0) width (480) height (360) padding (6) mode [read-only v] as [richtext1]`
- **Description:** Adds a rich text editor widget with width of W and height of H, centered at the position of (X, Y). This textbox can display or edit text with full formatting instead of plain text. The text inside the textbox will have a padding of P around the 4 borders. The MODETYPE can be 'read only' or 'input'. The last input is a name for the textbox and it can not be empty.
- **Can be used for 3D:** false

### Display Widgets

#### widget_addlabel
- **Block ID:** widget_addlabel
- **Syntax:** `add label [TEXT] at X (X) Y (Y) width (WIDTH) height (HEIGHT) padding (P) as [NAME]`
- **Usage Example:** `add label [Hi] at X (0) Y (0) width (100) height (30) padding (6) as [label1]`
- **Description:** Adds a label widget with the given WIDTH and HEIGHT, centered at the position of (X, Y). The text in the label has a padding of P around the 4 edges. The label will be given the NAME and it can not be blank. You can set the text shown on the label using the 'set value to [V] for widget [WIDGETNAME v]' block. You can read out the current text on the label using the 'value of widget [WIDGETNAME v]' block.
- **Can be used for 3D:** false

### Button Widgets

#### widget_addbutton
- **Block ID:** widget_addbutton
- **Syntax:** `add button [TEXT] at X (X) Y (Y) width (WIDTH) height (HEIGHT) tooltip [TOOLTIP] as [NAME]`
- **Usage Example:** `add button [Run] at X (0) Y (0) width (100) height (30) tooltip [Hi] as [button1]`
- **QuickDescription:** Adds a button widget
- **Description:** Adds a button with the given WIDTH and HEIGHT, centered at the position of (X, Y). The text shown on the button has a padding of P around the 4 edges. The button will be given the NAME and it can not be blank. To handle button click event, you can use the 'when widget [NAME v] clicked' block. You can set the text shown on the button using the 'set value to [V] for widget [WIDGETNAME v]' block. You can read out the current text on the button using the 'value of widget [WIDGETNAME v]' block.
- **Can be used for 3D:** false

#### widget_addradiobutton
- **Block ID:** widget_addradiobutton
- **Syntax:** `add radio buttons [CHOICE1] [CHOICE2] [CHOICE3] [CHOICE4] [CHOICE5] [CHOICE6] [ORIENTATION v] at x (0) y (0) width (200) height (30) named [NAME]`
- **Usage Example:** `add radio buttons [A] [B] [C] [D] [ ] [ ] [horizontal v] at x (X) y (Y) width (WIDTH) height (HEIGHT) named [rb1]`
- **Description:** Adds a group of radio buttons, centered at (X, Y), within a rectangle region of WIDTH and HEIGHT. There can be at most 6 buttons. Their text will be CHOICE1 to CHOICE6, and if any of these 6 inputs are empty, that button will not be displayed. The ORIENTATION can be 'vertial' or 'horizontal', which controls how the radio buttons are laid out. The radio button group is named as NAME.
- **Can be used for 3D:** false

#### widget_addcheckbox
- **Block ID:** widget_addcheckbox
- **Syntax:** `add checkbox at X (X) Y (Y) named [NAME]`
- **Usage Example:** `add checkbox at X (0) Y (0) named [checkbox1]`
- **Description:** Adds a checkbox at the position of (X, Y) and name it as NAME. The value of the checkbox widget will be 0 if it is unchecked and 1 if it is checked. You can set its value using the 'set value to [V] for widget [WIDGETNAME v]' block. You can read out the value using the 'value of widget [WIDGETNAME v]' block.
- **Can be used for 3D:** false

### Selection Widgets

#### widget_addslider
- **Block ID:** widget_addslider
- **Syntax:** `add slider at X (X) Y (Y) width (WIDTH) between (MIN) and (MAX) as [NAME]`
- **Usage Example:** `add slider at X (0) Y (0) width (200) between (0) and (100) as [slider1]`
- **Description:** Adds a slider widget centered at the specified position of (X, Y) with the given WIDTH. Name this slider as NAME. Its value range is between MIN and MAX. You can set its value using the 'set value to [V] for widget [WIDGETNAME v]' block. You can read out the value using the 'value of widget [WIDGETNAME v]' block.
- **Can be used for 3D:** false

#### widget_addmenu
- **Block ID:** widget_addmenu (dropdown menu)
- **Syntax:** `add dropdown menu at X (X) Y (Y) width (WIDTH) height (HEIGHT) using list [LIST v] as [NAME]`
- **Usage Example:** `add dropdown menu at X (0) Y (0) width (200) height (30) using list [names v] as [menu1]`
- **Description:** Adds a dropdown menu centered at the specified position of (X, Y) with the given WIDTH and HEIGHT. The choices of the dropdown will be defined by the items in the list LISTNAME. Name this slider as NAME. You can set its selected value using the 'set value to [V] for widget [WIDGETNAME v]' block. You can read out the selected choice using the 'value of widget [WIDGETNAME v]' block.
- **Can be used for 3D:** false

#### widget_adddatepicker
- **Block ID:** widget_adddatepicker
- **Syntax:** `add date picker at X (X) Y (Y) as [NAME]`
- **Usage Example:** `add date picker at X (0) Y (0) as [datepicker1]`
- **Description:** Adds a date picker widget centered at the specified position of (X, Y), and name this date picker as NAME. You can set its date value using the 'set value to [V] for widget [WIDGETNAME v]' block, such as 'set value to [20200512] for widget [datepicker1 v]'. You can read out the date selected by the user using the 'value of widget [WIDGETNAME v]' block, which will return a value like 20200512. The date picker's default size is 200 wide by 30 tall.
- **Can be used for 3D:** false

#### widget_addcolorpicker
- **Block ID:** widget_addcolorpicker
- **Syntax:** `add color picker at X (X) Y (Y) as [NAME]`
- **Usage Example:** `add color picker at X (0) Y (0) as [colorpicker1]`
- **Description:** Adds a color picker widget centered at the specified position of (X, Y), and name this color picker as NAME. You can set its color value using the 'set value to [V] for widget [WIDGETNAME v]' block, such as 'set value to [#FF00FFFF] for widget [colorpicker1 v]'. You can read out the color selected by the user using the 'value of widget [WIDGETNAME v]' block, which will return a value like #FFFF00FF.
- **Can be used for 3D:** false

### Image Widgets

#### widget_addimagefromcostumes
- **Block ID:** widget_addimagefromcostumes
- **Syntax:** `add image [COSTUMENAME v] at x (X) y (Y) width (WIDTH) height (HEIGHT) aspect ratio [OPTION v] as [NAME]`
- **Usage Example:** `add image [costume1 v] at x (0) y (0) width (480) height (360) aspect ratio [keep v] as [image1]`
- **Description:** Adds the costume named COSTUMENAME as an image widget to the stage, centered at the (X, Y) position, as a rectangle in WIDTH and HEIGHT. For aspect ratio, if OPTION is 'keep', the original aspect ratio will be kept for the image, and there may be some border area outside the image; or OPTION can be 'stretch', which will scale the image to fully occupy the rectangle area. Specify a NAME for the image widget using the last input.
- **Can be used for 3D:** false

#### widget_addimagefromurl
- **Block ID:** widget_addimagefromurl
- **Syntax:** `add image from URL [URL] at x (X) y (Y) width (WIDTH) height (HEIGHT) aspect ratio [OPTION v] as [NAME]`
- **Usage Example:** `add image from URL [https://play.creaticode.com/tcode-static-files/images/newlogo200.png] at x (0) y (0) width (480) height (360) aspect ratio [keep v] as []`
- **Description:** Adds the image shared at URL as an image widget to the stage, centered at the (X, Y) position, as a rectangle in WIDTH and HEIGHT. For aspect ratio, if OPTION is 'keep', the original aspect ratio will be kept for the image, and there may be some border area outside the image; or OPTION can be 'stretch', which will scale the image to fully occupy the rectangle area. Specify a NAME for the image widget using the last input.
- **Can be used for 3D:** false

#### widget_addimage
- **Block ID:** widget_addimage
- **Syntax:** `add image [COSTUMENAME v] to widget named [WIDGETNAME v] at position X (X) Y (Y)`
- **Usage Example:** `add image [costume1 v] to widget named [button1 v] at position X (0) Y (0)`
- **Description:** Adds the costume image named COSTUMENAME to the widget named WIDGETNAME at the position of (X, Y). This block is useful if you want to add a small image icon on another widget, such as a button or a label.
- **Can be used for 3D:** false

#### widget_addimageurl
- **Block ID:** widget_addimageurl
- **Syntax:** `add image at URL [URL] to widget named [WIDGETNAME v] at position X (X) Y (Y)`
- **Usage Example:** `add image at URL [https://play.creaticode.com/tcode-static-files/images/newlogo200.png] to widget named [button1 v] at position X (0) Y (0)`
- **Description:** Adds the image at the given URL to the widget named WIDGETNAME at the position of (X, Y). This block is useful if you want to add a small image icon on another widget, such as a button or a label.
- **Can be used for 3D:** false

### Camera Widget

#### widget_showcamera
- **Block ID:** widget_showcamera
- **Syntax:** `show [SIDE v] camera in [MODE v] x (X) y (Y) width (W) height (H) as [NAME]`
- **Usage Example:** `show [front v] camera in [normal v] x (0) y (0) width (480) height (360) as [camera1]`
- **Description:** Adds a camera window widget with width of W and height of H, centered at the position of (X, Y). It will be showing images from the 'front' or 'back' camera as specified by SIDE, and MODE can be 'normal' or 'flipped'. The last input is a name for the textbox and it can not be empty.
- **Can be used for 3D:** false

#### widget_savepicturefromcamera
- **Block ID:** widget_savepicturefromcamera
- **Syntax:** `save picture from camera [CAMERAWIDGETNAME v] as costume [COSTUMENAME]`
- **Usage Example:** `save picture from camera [camera1 v] as costume [picture1]`
- **Description:** Takes a snapshot of the camera view from the camera widget named CAMERAWIDGETNAME, and save it as a costume of this sprite with the name of COSTUMENAME.
- **Can be used for 3D:** false

### Video Widget

#### widget_addvideo
- **Block ID:** widget_addvideo
- **Syntax:** `add youtube video [URL] at X (X) Y (Y) width (WIDTH) height (HEIGHT) named [NAME] in [LAYER v]`
- **Usage Example:** `add youtube video [https://www.youtube.com/watch?v=_-Dm2LTXC88] at X (0) Y (0) width (480) height (360) named [video1] in (foreground v)`
- **Description:** Adds a YouTube video widget to the stage.
- **Can be used for 3D:** false

#### widget_actionvideo
- **Block ID:** widget_actionvideo
- **Syntax:** `[COMMAND v] video for [VIDEONAME v]`
- **Usage Example:** `[start v] video for [video1 v]`
- **Description:** Run a COMMAND on the video widget named VIDEONAME: start, pause, stop, mute or unmute.
- **Can be used for 3D:** false

#### widget_seektosecondsvideo
- **Block ID:** widget_seektosecondsvideo
- **Syntax:** `seek to (TIME) seconds in video named [VIDEONAME v]`
- **Usage Example:** `seek to (100) seconds in video named [video1 v]`
- **Description:** Seeks to the time of TIME (in seconds) in the video widget named VIDEONAME.
- **Can be used for 3D:** false

#### widget_currentvideotime
- **Block ID:** widget_currentvideotime
- **Syntax:** `current video time for [VIDEONAME v]`
- **Usage Example:** `current video time for [video1 v]`
- **Description:** A reporter block for the current playing time in seconds of the youtube video named VIDEONAME.
- **Can be used for 3D:** false

#### widget_setyoutubevolume
- **Block ID:** widget_setyoutubevolume
- **Syntax:** `set volume to (VOLUME) for [VIDEONAME v]`
- **Usage Example:** `set volume to (50) for [video1 v]`
- **Description:** Sets the sound volume to VOLUME for the youtube video named VIDEONAME. VOLUME should be a number between 0 and 100.
- **Can be used for 3D:** false

#### widget_setyoutubeplaybackspeedratio
- **Block ID:** widget_setyoutubeplaybackspeedratio
- **Syntax:** `set playback speed ratio (SPEED) for [VIDEONAME v]`
- **Usage Example:** `set playback speed ratio (125) for [video1 v]`
- **Description:** Sets the playback speed ratio as SPEED for the youtube video named VIDEONAME. For example, if SPEED is 100, then the video is playing at normal speed. If SPEED is 200, then the speed will be doubled.
- **Can be used for 3D:** false

#### widget_whenvideotimeis
- **Block ID:** widget_whenvideotimeis
- **Syntax:** `when video time is (T) seconds for [VIDEONAME v]`
- **Usage Example:** `when video time is (10) seconds for [video1 v]`
- **Description:** A hat-block that is triggered when the video widget named VIDEONAME reaches the time point of T seconds into the video.
- **Can be used for 3D:** false

#### widget_whenvideoispaused
- **Block ID:** widget_whenvideoispaused
- **Syntax:** `when video [VIDEONAME v] paused`
- **Usage Example:** `when video [video1 v] paused`
- **Description:** A hat-block that is triggered when the video widget named VIDEONAME is paused.
- **Can be used for 3D:** false

#### widget_whenvideoisstopped
- **Block ID:** widget_whenvideoisstopped
- **Syntax:** `when video [VIDEONAME v] stopped`
- **Usage Example:** `when video [video1 v] stopped`
- **Description:** A hat-block that is triggered when the video widget named VIDEONAME is stopped.
- **Can be used for 3D:** false

#### widget_whenvideostart
- **Block ID:** widget_whenvideostart
- **Syntax:** `when video [VIDEONAME v] start`
- **Usage Example:** `when video [video1 v] start`
- **Description:** A hat-block that is triggered when the video widget named VIDEONAME starts playing.
- **Can be used for 3D:** false

### Chart Widgets

#### widget_drawchartusinglist
- **Block ID:** widget_drawchartusinglist
- **Syntax:** `draw [CHARTTYPE v] chart using list [LISTNAME v] x (X) y (Y) width (WIDTH) height (HEIGHT)`
- **Usage Example:** `draw [line v] chart using list [list1 v] x (0) y (0) width (100) height (100)`
- **Description:** Draws a chart of the selected CHARTTYPE, which can be 'line', 'bar', 'pie' or 'percentage', with the data in the list named LISTNAME. Since only a single list of data points is provided to draw the chart, the X axis of the chart will be labeld using each data point's index, starting at 1. The Y axis of the chart will be the value range of all the data points in the list. The chart will center at the (X, Y) position on the stage, with the size of WIDTH and HEIGHT.
- **Can be used for 3D:** false

#### widget_drawchartusingcolumn
- **Block ID:** widget_drawchartusingcolumn
- **Syntax:** `draw [CHARTTYPE v] chart using columns [COLUMNLIST] from table [TABLENAME v] x (X) y (Y) width (WIDTH) height (HEIGHT)`
- **Usage Example:** `draw [line v] chart using columns [age,height] from table [k v] x (0) y (0) width (100) height (100)`
- **QuickDescription:** Draws a chart of the selected CHARTTYPE
- **Description:** Draws a chart using data from multiple columns in a table.
- **Can be used for 3D:** false

#### widget_drawchartusingcategory
- **Block ID:** widget_drawchartusingcategory
- **Syntax:** `draw pie chart using category [CATEGORYCOLUMN] and value [VALUECOLUMN] from table [TABLENAME v] x (X) y (Y) width (WIDTH) height (HEIGHT)`
- **Usage Example:** `draw pie chart using category [grade] and value [height] from table [student table v] x (0) y (0) width (100) height (100)`
- **Description:** Draws a pie chart using data from the table named TABLENAME. The data from the column named VALUECOLUMN will be used to calculate the percentage of each row, and the data from the column named CATEGORYCOLUMN will be used as labels in the pie chart for each row. The chart will center at the (X, Y) position on the stage, with the size of WIDTH and HEIGHT.
- **Can be used for 3D:** false

### Progress Bar Widget

#### widget_progressbar
- **Block ID:** widget_progressbar
- **Syntax:** `add progress bar as (CURRENT) out of total (TOTAL) at x (X) y (Y) width (WIDTH) height (HEIGHT) color [COLOR] background [BG] border width (BORDERWIDTH) color [BORDERCOLOR] as [NAME]`
- **Usage Example:** `add progress bar as (50) out of total (100) at x (0) y (0) width (200) height (20) color [#1777FFFF] background [#F0F0F0FF] border width (0) color [#F0F0F0FF] as [progressbar1]`
- **QuickDescription:** Adds a progress bar widget
- **Description:** Adds a progress bar widget with customizable current value, total value, position, size, and colors.
- **Can be used for 3D:** false

### Chat Window Widget

#### widget_createchatwindow
- **Block ID:** widget_createchatwindow
- **Syntax:** `add chat window x (X) y (Y) width (WIDTH) height (HEIGHT) input rows (ROWS) background [BG] border [BORDERCOLOR] name [NAME]`
- **Usage Example:** `add chat window x (0) y (0) width (480) height (360) input rows (1) background [#F0F0F0FF] border [#000000FF] name [chat1]`
- **Description:** Adds a chat window widget to the stage, centered at the position (X, Y) with dimension of WIDTH and HEIGHT. The chat window has 2 parts. At the bottom is a wide input box on the left and a send button on the right. On the top is a chat history panel for displaying all previous messages in the chat.
- **Can be used for 3D:** false

#### widget_appendchatmessage
- **Block ID:** widget_appendchatmessage
- **Syntax:** `append to chat [CHATNAME v] message [MESSAGE] as [SENDER] icon [ICON v] align [ALIGN v] text size (TEXTSIZE) color [COLOR] background [BG]`
- **Usage Example:** `append to chat [chat1 v] message [hi] as [Joe] icon [ROBOT v] align [Left v] text size (14) color [#000000FF] background [#F0F0F0FF]`
- **QuickDescription:** Appends a new MESSAGE to the chat history panel of the chat window named CHATNAME
- **Description:** Appends a formatted message to a chat window with customizable sender, icon, alignment, text size, and colors.
- **Can be used for 3D:** false

#### widget_updatelastchatmessage
- **Block ID:** widget_updatelastchatmessage
- **Syntax:** `update last chat message to [MESSAGE] for chat [CHATNAME v]`
- **Usage Example:** `update last chat message to [good morning] for chat [chat1 v]`
- **Description:** Updates the last message in the chat history panel of the chat window named CHATNAME. MESSAGE will be the new content for that message. This is useful if the last message is being typed in by a remote user in a distributed chat, or it is being generated in streaming mode by a chatbot.
- **Can be used for 3D:** false

### Tab Widget

#### widget_addtabs
- **Block ID:** widget_addtabs
- **Syntax:** `create tabs at X (X) Y (Y) width (WIDTH) height (HEIGHT) names [TAB1] [TAB2] [TAB3] [TAB4] [TAB5] [TAB6] [TAB7] [TAB8] show heading [SHOWHEADING v]`
- **Usage Example:** `create tabs at X (0) Y (0) width (480) height (360) names [t1] [t2] [] [] [] [] [] [] show heading [Yes v]`
- **Description:** Creates a tabs widget centered at (X, Y), with the given WIDTH and HEIGHT. You can specify up to 8 tab names of TAB1 to TAB8, and blank tab names are ignored. The SHOWHEADING option can be set to 'Yes' or 'No'.
- **Can be used for 3D:** false

#### widget_selecttab
- **Block ID:** widget_selecttab
- **Syntax:** `select tab [TABNAME]`
- **Usage Example:** `select tab [t1]`
- **Description:** Selects the tab named TABNAME, bringing it to the foreground with all the widgets inside that tab.
- **Can be used for 3D:** false

#### widget_settabcontainer
- **Block ID:** widget_settabcontainer
- **Syntax:** `set tab container [TABNAME v]`
- **Usage Example:** `set tab container [t1 v]`
- **Description:** Sets the tab named TABNAME as the widget container, so all widgets added after this block will be added into this tab.
- **Can be used for 3D:** false

#### widget_showhidetabnamed
- **Block ID:** widget_showhidetabnamed
- **Syntax:** `[ACTION v] tab named [TABNAME]`
- **Usage Example:** `[show v] tab named [t1]`
- **Description:** Take an ACTION on the tab named TABNAME. The ACTION can be 'show' or 'hide' to change visibility of the tab, or 'add' and 'remove' to add or remove a tab.
- **Can be used for 3D:** false

#### widget_whentabselected
- **Block ID:** widget_whentabselected
- **Syntax:** `when tab [TABNAME v] selected`
- **Usage Example:** `when tab [t1 v] selected`
- **Description:** A hat-block that is triggered when the tab named TABNAME is selected and displayed.
- **Can be used for 3D:** false

### Link Widget

#### widget_addlink
- **Block ID:** widget_addlink
- **Syntax:** `add link at X (X) Y (Y) url [URL] as [NAME]`
- **Usage Example:** `add link at X (0) Y (0) url [google.com] as [link1]`
- **Description:** Adds a hyperlink widget centered at the (X, Y) position that links to the given URL. Assign the widget a name of NAME.
- **Can be used for 3D:** false

### Toolbox Widget

#### widget_addtoolbox
- **Block ID:** widget_addtoolbox
- **Syntax:** `add toolbox at x (X) y (Y) width (WIDTH) height (HEIGHT) row count (ROWCOUNT) column count (COLCOUNT) as [NAME]`
- **Usage Example:** `add toolbox at x (0) y (0) width (250) height (50) row count (1) column count (5) as [tb]`
- **QuickDescription:** Adds a toolbox widget, which is a grid of icons. It looks similar to the toolbox in MineCraft.
- **Description:** Adds a toolbox widget (grid of icons) similar to MineCraft's toolbox.
- **Can be used for 3D:** false

#### widget_seticontotoolbox
- **Block ID:** widget_seticontotoolbox
- **Syntax:** `set icon to [COSTUMENAME v] at row (ROW) column (COLUMN) for toolbox [TOOLBOXNAME v]`
- **Usage Example:** `set icon to [costume1 v] at row (1) column (1) for toolbox [tb v]`
- **Description:** Set the icon at the given ROW and COLUMN of the toolbox named TOOLBOXNAME to the costume image named COSTUMENAME. For example, to set the first icon in the first row, set both ROW and COLUMN to 1.
- **Can be used for 3D:** false

### Widget Value and Text Operations

#### widget_valuefromwidget
- **Block ID:** widget_valuefromwidget
- **Syntax:** `value of widget [WIDGETNAME v]`
- **Usage Example:** `value of widget [button1 v]`
- **QuickDescription:** A reporter block that returns the current value of the widget with the given name of WIDGETNAME.
- **Description:** Returns the current value of any widget by its name.
- **Can be used for 3D:** false

#### widget_settext
- **Block ID:** widget_settext
- **Syntax:** `set value to [V] for widget [WIDGETNAME v]`
- **Usage Example:** `set value to [hi] for widget [t1 v]`
- **Description:** Sets the value for a widget by its name.
- **Can be used for 3D:** false

#### widget_appendtext
- **Block ID:** widget_appendtext
- **Syntax:** `append text [NEWTEXT] to [WIDGETNAME v] in new line [ISNEWLINE v]`
- **Usage Example:** `append text [22] to [button1 v] in new line [No v]`
- **Description:** Appends the text of NEWTEXT to the specified widget named WIDGETNAME, such as a textbox or a button. If NEWLINE is 'Yes', then the NEWTEXT will appear in a new line, otherwise it will be appended to the last existing line.
- **Can be used for 3D:** false

### Widget Styling

#### widget_settextstyle
- **Block ID:** widget_settextstyle
- **Syntax:** `set text style [FONTSTYLE v] font size (FONTSIZE) text color [TEXTCOLOR] boldness [BOLDNESS v] text alignment [TEXTALIGNMENT v] for widget [WIDGETNAME v]`
- **Usage Example:** `set text style [sans-serif v] font size (18) text color [#FFFFFFFF] boldness [normal v] text alignment [Middle v] for widget [button1 v]`
- **QuickDescription:** Sets the text style for the widget named WIDGETNAME
- **Description:** Sets comprehensive text styling including font, size, color, boldness, and alignment for a widget.
- **Can be used for 3D:** false

#### widget_setwidgetstyle
- **Block ID:** widget_setwidgetstyle
- **Syntax:** `set widget background color [BACKGROUNDCOLOR] border color [BORDERCOLOR] border width (BORDERWIDTH) border radius (BORDERRADIUS) for [WIDGETNAME v]`
- **Usage Example:** `set widget background color [#7531BBBD] border color [#E6E6E6FF] border width (1) border radius (4) for [button1 v]`
- **Description:** This block updates the style of the widget named WIDGETNAME. Including the BACKGROUNDCOLOR, BORDERCOLOR, BORDERWIDTH, and BORDERRADIUS. The color parameters accept the #RRGGBBAA format, so you can set some transparency to the widget using this block as well. This block works on almost all widget types, such as button, label, text box, dropdown menu, etc.
- **Can be used for 3D:** false

### Widget Transformation

#### widget_movewidgettoxy
- **Block ID:** widget_movewidgettoxy
- **Syntax:** `move widget [WIDGETNAME v] to X (X) Y (Y) in (T) seconds [BLOCKINGMODE v]`
- **Usage Example:** `move widget [button1 v] to X (0) Y (0) in (0) seconds [blocking v]`
- **Description:** Moves a widget to a new position over time with optional blocking mode.
- **Can be used for 3D:** false

#### widget_resizewidgettowidthheight
- **Block ID:** widget_resizewidgettowidthheight
- **Syntax:** `resize widget [WIDGETNAME v] to width (WIDTH) height (HEIGHT) in (T) seconds [BLOCKINGMODE v]`
- **Usage Example:** `resize widget [button1 v] to width (100) height (100) in (0) seconds [blocking v]`
- **Description:** Resizes the widget named WIDGETNAME to the given WIDTH and HEIGHT over T seconds. If BLOCKINGMODE is 'blocking', then this block will wait until the resizing is completed before running the next block. If 'non-blocking', the next block will start to run right away even if the resizing animation is not completed.
- **Can be used for 3D:** false

#### widget_scalewidgettowidthheight
- **Block ID:** widget_scalewidgettowidthheight
- **Syntax:** Similar to resize
- **Description:** Scales a widget to new dimensions.
- **Can be used for 3D:** false

#### widget_rotatewidgetbydegrees
- **Block ID:** widget_rotatewidgetbydegrees
- **Syntax:** Rotate widget by degrees
- **Description:** Rotates a widget by specified degrees.
- **Can be used for 3D:** false

#### widget_transparencytowidget
- **Block ID:** widget_transparencytowidget
- **Syntax:** Set transparency for widget
- **Description:** Sets the transparency level for a widget.
- **Can be used for 3D:** false

### Widget Visibility and Management

#### widget_setvisibility
- **Block ID:** widget_setvisibility
- **Syntax:** `set visibility [VISIBILITY v] for widget named [WIDGETNAME v]`
- **Usage Example:** `set visibility [show v] for widget named [button1 v]`
- **Description:** Sets the visibility to VISIBILITY (show or hide) for the widget named WIDGETNAME.
- **Can be used for 3D:** false

#### widget_setvisibilityforall
- **Block ID:** widget_setvisibilityforall
- **Syntax:** `set visibility [VISIBILITY v] for all widgets`
- **Usage Example:** `set visibility [show v] for all widgets`
- **Description:** Sets the visibility to VISIBILITY (show or hide) for all widgets in the project.
- **Can be used for 3D:** false

#### widget_setzindex
- **Block ID:** widget_setzindex
- **Syntax:** `set z-index to [ZINDEX] for widget named [WIDGETNAME v]`
- **Usage Example:** `set z-index to [20] for widget named [button1 v]`
- **Description:** Sets the z-index of the given widget. All widgets have default z-index of 10.
- **Can be used for 3D:** false

#### widget_removewidget
- **Block ID:** widget_removewidget
- **Syntax:** `remove widget named [WIDGETNAME v]`
- **Usage Example:** `remove widget named [button1 v]`
- **Description:** Removes the widget named WIDGETNAME from the project.
- **Can be used for 3D:** false

#### widget_removeallwidgets
- **Block ID:** widget_removeallwidgets
- **Syntax:** `remove all widgets`
- **Usage Example:** `remove all widgets`
- **Description:** Removes all widgets from the project.
- **Can be used for 3D:** false

#### widget_disablewidget
- **Block ID:** widget_disablewidget
- **Syntax:** `[ACTION v] widget [WIDGETNAME v]`
- **Usage Example:** `[Disable v] widget [button1 v]`
- **Description:** Enables or disables a widget.
- **Can be used for 3D:** false

### Widget Event Handlers

#### widget_whenwidgetclicked
- **Block ID:** widget_whenwidgetclicked
- **Syntax:** `when widget [NAME v] clicked`
- **Usage Example:** `when widget (button1 v) clicked`
- **Description:** A hat-block that is triggered whenever the widget with the given NAME is clicked. This block can be used to handle user click events for widget like button, image, radio button.
- **Can be used for 3D:** false

#### widget_whenwidgetchanges
- **Block ID:** widget_whenwidgetchanges
- **Syntax:** `when widget [NAME v] changes`
- **Usage Example:** `when widget [textbox1 v] changes`
- **Description:** A hat-block that is triggered when the widget with the given NAME changes its state or value. This block can be used to handle user actions that change the value of a widget, such as text box, dropdown menu, slider, color picker, date picker, etc.
- **Can be used for 3D:** false

#### widget_whenmouseenter
- **Block ID:** widget_whenmouseenter
- **Syntax:** `when pointer enters widget named [WIDGETNAME v]`
- **Usage Example:** `when pointer enters widget named [button1 v]`
- **Description:** A hat-block that is triggered when the pointer enters the area over the widget named WIDGETNAME.
- **Can be used for 3D:** false

#### widget_whenmouseleave
- **Block ID:** widget_whenmouseleave
- **Syntax:** `when pointer leaves widget named [WIDGETNAME v]`
- **Usage Example:** `when pointer leaves widget named [button1 v]`
- **Description:** A hat-block that is triggered when the pointer leaves the area over the widget named WIDGETNAME.
- **Can be used for 3D:** false

### Other Widget Operations

#### widget_confirmtextwithbuttons
- **Block ID:** widget_confirmtextwithbuttons
- **Syntax:** Confirm dialog with custom buttons
- **Description:** Shows a confirmation dialog with customizable buttons.
- **Can be used for 3D:** false

#### widget_whenanybuttonnamedclicked
- **Block ID:** widget_whenanybuttonnamedclicked
- **Syntax:** When any button named [NAME] clicked
- **Description:** Hat block triggered when any button with a specific pattern is clicked.
- **Can be used for 3D:** false

#### widget_releasefocus
- **Block ID:** widget_releasefocus
- **Syntax:** Release focus from widget
- **Description:** Removes focus from the currently focused widget.
- **Can be used for 3D:** false

#### widget_runproject
- **Block ID:** widget_runproject
- **Syntax:** `run project [PROJECTID] in [BROWSERTAB v] browser tab`
- **Usage Example:** `run project [23423sdffd] in [new v] browser tab`
- **Description:** Runs another CreatiCode project in a browser tab.
- **Can be used for 3D:** false

#### widget_opennewtabwithurl
- **Block ID:** widget_opennewtabwithurl
- **Syntax:** Open new tab with URL
- **Description:** Opens a URL in a new browser tab.
- **Can be used for 3D:** false

#### widget_applylayoutrowheightcellwidth
- **Block ID:** widget_applylayoutrowheightcellwidth
- **Syntax:** Apply layout with row height and cell width
- **Description:** Applies grid layout to widgets with specified row height and cell width.
- **Can be used for 3D:** false

#### widget_addmenubar
- **Block ID:** widget_addmenubar
- **Syntax:** `add menu bar at X (X) Y (Y) width (WIDTH) height (HEIGHT) as [NAME]`
- **Usage Example:** `add menu bar at X (0) Y (0) width (250) height (50) as [menubar1]`
- **Description:** Adds a menu bar widget for creating application-style menus.
- **Can be used for 3D:** false

#### widget_addmenugroup
- **Block ID:** widget_addmenugroup
- **Syntax:** Add menu group to menu bar
- **Description:** Adds a menu group (dropdown) to a menu bar.
- **Can be used for 3D:** false

#### widget_addmenuitem
- **Block ID:** widget_addmenuitem
- **Syntax:** Add menu item to menu group
- **Description:** Adds a menu item to a menu group.
- **Can be used for 3D:** false

#### widget_deletecostume
- **Block ID:** widget_deletecostume
- **Syntax:** Delete costume from widget
- **Description:** Deletes a costume/image from a widget.
- **Can be used for 3D:** false

---

## AI SPEECH AND TEXT-TO-SPEECH CATEGORY

### Speech Recognition (Azure)

#### ai_startspeech
- **Block ID:** ai_startspeech
- **Category:** AI
- **Syntax:** `start recognizing speech in [LANGUAGE v] record as [SOUNDNAME]`
- **Usage Example:** `start recognizing speech in [English (United States) v] record as []`
- **Description:** Turn on microphone to start recording voice input to prepare for recognition in the specified LANGUAGE. The speech recognition will only end when the 'end speech recognition' block runs. That block will call Microsoft Azure API to recognize the recorded speech in the specified LANGUAGE, and the recognized text can be retrieved using the 'text from speech' reporter block.
- **Can be used for 3D:** false

#### ai_endspeech
- **Block ID:** ai_endspeech
- **Category:** AI
- **Syntax:** `end speech recognition`
- **Usage Example:** `end speech recognition`
- **Description:** Stops recording voice input on the microphone and send the recorded speech sound to speech recognition API, and then store the recognized text in the 'text from speech' reporter block. The API can be Microsoft Azure API or OpenAI Whisper API. It depends on which block is used to start the speech recognition: 'start recognizing speech in [LANGUAGE v] record as [SOUNDNAME]' or 'OpenAI: start recognizing speech in [LANGUAGE v] record as [SOUNDNAME]'.
- **Can be used for 3D:** false

#### ai_startrecognizer (Continuous Speech Recognition)
- **Block ID:** ai_startrecognizer
- **Category:** AI
- **Syntax:** `start continuous speech recognition in [LANGUAGE v] into list [LISTNAME v]`
- **Usage Example:** `start continuous speech recognition in [English (United States) v] into list [k v]`
- **Description:** Starts to record voice input from the microphone and stream it to Microsoft Azure API, which recognizes the speech text in the given LANGUAGE, and returns the recognized parts of the speech continuously.
- **Can be used for 3D:** false

#### ai_stoprecognizer
- **Block ID:** ai_stoprecognizer
- **Category:** AI
- **Syntax:** `stop continuous speech recognition`
- **Usage Example:** `stop continuous speech recognition`
- **Description:** Stops continuous speech recognition.
- **Can be used for 3D:** false

### Speech Recognition (OpenAI Whisper)

#### ai_startopenaispeech
- **Block ID:** ai_startopenaispeech
- **Category:** AI
- **Syntax:** `OpenAI: start recognizing speech in [LANGUAGE v] record as [SOUNDNAME]`
- **Usage Example:** `OpenAI: start recognizing speech in [English v] record as []`
- **Description:** Turn on microphone to start recording voice input to prepare for recognition in the specified LANGUAGE. The speech recognition will only end when the 'end speech recognition' block runs. That block will the OpenAI Whisper API to recognize the recorded speech in the specified LANGUAGE, and the recognized text can be retrieved using the 'text from speech' reporter block.
- **Can be used for 3D:** false

### Speech Recognition Common Blocks

#### ai_textfromspeech
- **Block ID:** ai_textfromspeech
- **Category:** AI
- **Syntax:** `text from speech`
- **Usage Example:** `text from speech`
- **Description:** A reporter block that returns the text recognized from speech.
- **Can be used for 3D:** false

#### ai_clearspeech
- **Block ID:** ai_clearspeech
- **Category:** AI
- **Syntax:** `clear speech text`
- **Usage Example:** `clear speech text`
- **Description:** Clears the content of the 'text from speech' block.
- **Can be used for 3D:** false

### Text-to-Speech (Azure)

#### ai_speakinlanguage
- **Block ID:** ai_speakinlanguage
- **Category:** AI
- **Syntax:** `say [TEXT] in [LANGUAGE v] as [VOICETYPE v] speed (SPEEDRATIO) pitch (PITCHRATIO) volume (VOLUMERATIO) store sound as [SOUNDNAME]`
- **Usage Example:** `say [Hi] in [English (United States) v] as [Male v] speed (100) pitch (100) volume (100) store sound as []`
- **Description:** Converts the given TEXT to audio in the specified LANGUAGE using text-to-speech API from Microsoft Azure in the given VOICETYPE. Parameters:
  - TEXT: The text to convert to speech
  - LANGUAGE: The language and locale (e.g., "English (United States)")
  - VOICETYPE: The voice type (Male, Female, or specific voice names)
  - SPEEDRATIO: Speech speed (100 = normal speed)
  - PITCHRATIO: Voice pitch (100 = normal pitch)
  - VOLUMERATIO: Volume level (100 = normal volume)
  - SOUNDNAME: Optional name to store the generated sound as a sound effect
- **Can be used for 3D:** false

#### ai_stopspeaking
- **Block ID:** ai_stopspeaking
- **Category:** AI
- **Syntax:** `stop speaking`
- **Usage Example:** `stop speaking`
- **Description:** Stop the AI speech from the text to speech block.
- **Can be used for 3D:** false

---

## SUMMARY

This reference document covers all blocks in the following categories from blockdes8.txt:

### Looks Category (30 blocks)
- Display control (show/hide)
- Speech and thought bubbles with styling
- Size control (set, change, reduce)
- Visual effects (fade, reveal)
- Text printing on stage and costumes
- Drawing shapes on costumes (rectangles, ovals, lines, curves)
- Costume management (add from URL, export, snapshot)
- Stage properties (mode, width, height, layer)
- Color creation with HSBT

### Widgets Category (70+ blocks)
- **Text Input:** Textbox, Rich textbox
- **Display:** Label, Image (from costumes/URLs)
- **Buttons:** Button, Radio button, Checkbox
- **Selection:** Slider, Dropdown menu, Date picker, Color picker
- **Media:** Camera, YouTube video
- **Charts:** Line, Bar, Pie, Percentage charts
- **Advanced:** Progress bar, Chat window, Tabs, Toolbox, Link, Menu bar
- **Widget Management:** Value operations, styling, transformation, visibility, removal
- **Event Handlers:** Click, change, mouse enter/leave events

### AI Speech and Text-to-Speech Category (10 blocks)
- **Speech Recognition (Azure):** Start, end, continuous mode
- **Speech Recognition (OpenAI Whisper):** Start recognition
- **Common:** Text from speech reporter, clear speech text
- **Text-to-Speech (Azure):** Say text with voice, speed, pitch, volume control
- **Control:** Stop speaking

---

## KEY FEATURES FOR T15 SKILLS

### Say/Think Bubbles
- Full styling support: font size, font color, background color, edge color
- Timed or permanent display
- Both speech and thought bubble variants

### Text Display Options
1. **Speech/Thought Bubbles:** Attached to sprites with styling
2. **Print Text:** Positioned text on stage with sizing
3. **Draw Text:** Text drawn directly on costumes
4. **Labels:** Widget-based text display with full styling
5. **Textboxes:** Single or multi-line, read-only or input mode
6. **Rich Textboxes:** Full formatting support

### Drawing on Costumes
- Rectangles (with corner radius, rotation)
- Ovals (with rotation)
- Lines (with thickness)
- Bezier curves (with control points)
- Text (with size, color, rotation)
- All drawings support RGBA color format (#RRGGBBAA)

### Widget Styling
- Text styling: font family, size, color, boldness, alignment
- Widget styling: background color, border color, border width, border radius
- All support RGBA transparency
- Transformation: move, resize, rotate, transparency

### Speech and Text-to-Speech
- **Two Speech Recognition APIs:** Microsoft Azure and OpenAI Whisper
- **Continuous Speech Recognition:** Real-time streaming to list
- **Text-to-Speech:** Microsoft Azure with customizable voice, speed, pitch, volume
- **Multiple Languages:** Support for various languages and locales
- **Sound Storage:** Optional storage of generated speech as sound effects

### Charts and Data Visualization
- Chart types: line, bar, pie, percentage
- Data sources: lists, table columns, category/value pairs
- Full positioning and sizing control
- Integration with data tables

### Advanced Widgets
- **Chat Window:** Full chat interface with history panel and input
- **Tabs:** Multi-tab interface with up to 8 tabs
- **Toolbox:** MineCraft-style icon grid
- **Progress Bar:** Customizable progress indication
- **Video:** YouTube video embedding with full control
- **Menu Bar:** Application-style menu system
