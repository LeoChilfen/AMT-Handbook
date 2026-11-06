# Layout & Forming

> 机体 Ch 04 · Layout & Forming · 原文 PDF 第 220 页

## 1. 原文

### Terminology

The following terms are commonly used in sheet metal forming and flat pattern layout. Familiarity with these terms aids in understanding how bend calculations are used in a bending operation. Figure 4-120 illustrates most of these terms.

Base measurement—the outside dimensions of a formed part. Base measurement is given on the drawing or blueprint or may be obtained from the original part.

Leg—the longer part of a formed angle.

Flange—the shorter part of a formed angle—the opposite of leg. If each side of the angle is the same length, then each is known as a leg.

Grain of the metal—natural grain of the material is formed as the sheet is rolled from molten ingot. Bend lines should be made to lie at a 90º angle to the grain of the metal if possible.

Bend allowance (BA)—refers to the curved section of metal within the bend (the portion of metal that is curved in bending). The bend allowance may be considered as being the length of the curved portion of the neutral line.

Bend radius—the arc is formed when sheet metal is bent. This arc is called the bend radius. The bend radius is measured from a radius center to the inside surface of the metal. The minimum bend radius depends on the temper, thickness, and type of material. Always use a Minimum Bend Radius Table to determine the minimum bend radius for the alloy that is going to be used. Minimum bend radius charts can be found in manufacturer’s maintenance manuals.

Bend tangent line (BL)—the location at which the metal starts to bend and the line at which the metal stops curving. All the space between the bend tangent lines is the bend allowance.

Neutral axis—an imaginary line that has the same length after bending as it had before bending. After bending, the bend area is 10 to 15 percent thinner than before bending. This thinning of the bend area moves the neutral line of the metal in towards the radius center. For calculation purposes, it is often assumed that the neutral axis is located at the center of the material, although the neutral axis is not exactly in the center of the material. However, the amount of error incurred is so slight that, for most work, assuming it is at the center is satisfactory.

Mold line (ML)—an extension of the flat side of a part beyond the radius.

Mold line dimension (MLD)—the dimension of a part made by the intersection of mold lines. It is the dimension the part would have if its corners had no radius.

Mold point—the point of intersection of the mold lines. The mold point would be the outside corner of the part if there were no radius.

K-Factor—the percentage of the material thickness where there is no stretching or compressing of the material, such as the neutral axis. This percentage has been calculated and is one of 179 numbers on the K chart corresponding to one of the angles between 0° and 180° to which metal can be bent. Whenever metal is to be bent to any angle other than 90° (K-factor of 90° equal to 1), the corresponding K-factor number is selected from the chart and is multiplied by the sum of the radius (R) and the thickness (T) of the metal. The product is the amount of setback (see next paragraph) for the bend. If no K chart is available, the K-factor can be calculated with a calculator by using the following formula: the K value is the tangent of one-half the bend angle.

Setback (SB)—the distance the jaws of a brake must be setback from the mold line to form a bend. In a 90° bend, SB = R + T (radius of the bend plus thickness of the metal). The setback dimension must be determined prior to making the bend because setback is used in determining the location of the beginning bend tangent line. When a part has more than one bend, setback must be subtracted for each bend. The majority of bends in sheet metal are 90° bends. The K-factor must be used for all bends that are smaller or larger than 90°.

Sight line—also called the bend or brake line, it is the layout line on the metal being formed that is set even with the nose of the brake and serves as a guide in bending the work.

Flat—that portion of a part that is not included in the bend. It is equal to the base measurement (MLD) minus the setback. Flat = MLD – SB Closed angle—an angle that is less than 90° when measured between legs, or more than 90° when the amount of bend is measured.

Open angle—an angle that is more than 90° when measured between legs, or less than 90° when the amount of bend is measured.

Total developed width (TDW)—the width of material measured around the bends from edge to edge. Finding the TDW is necessary to determine the size of material to be cut. The TDW is less than the sum of mold line dimensions since the metal is bent on a radius and not to a square corner as mold line dimensions indicate.

### Layout or Flat Pattern Development

To prevent any waste of material and to get a greater degree of accuracy in the finished part, it is wise to make a layout or flat pattern of a part before forming it. Construction of interchangeable structural and nonstructural parts is achieved by forming flat sheet stock to make channel, angle, zee, or hat section members. Before a sheet metal part is formed, make a flat pattern to show how much material is required in the bend areas, at what point the sheet must be inserted into the forming tool, or where bend lines are located. Bend lines must be determined to develop a flat pattern for sheet metal forming.

When forming straight angle bends, correct allowances must be made for setback and bend allowance. If shrinking or stretching processes are to be used, allowances must be made so that the part can be turned out with a minimum amount of forming.

### Making Straight Line Bends

When forming straight bends, the thickness of the material, its alloy composition, and its temper condition must be considered. Generally speaking, the thinner the material is, the more sharply it can be bent (the smaller the radius of bend), and the softer the material is, the sharper the bend is. Other factors that must be considered when making straight line bends are bend allowance, setback, and brake or sight line.

The radius of bend of a sheet of material is the radius of the bend as measured on the inside of the curved material. The minimum radius of bend of a sheet of material is the sharpest curve, or bend, to which the sheet can be bent without critically weakening the metal at the bend. If the radius of bend is too small, stresses and strains weaken the metal and may result in cracking.

A minimum radius of bend is specified for each type of aircraft sheet metal. The minimum bend radius is affected by the kind of material, thickness of the material, and temper condition of the material. Annealed sheet can be bent to a radius approximately equal to its thickness. Stainless steel and 2024-T3 aluminum alloy require a fairly large bend radius.

#### Bending a U-Channel

To understand the process of making a sheet metal layout, the steps for determining the layout of a sample U-channel will be discussed. When using bend allowance calculations, the following steps for finding the total developed length can be computed with formulas, charts, or computer-aided design (CAD) and computer-aided manufacturing (CAM) software packages. This channel is made of 0.040-inch 2024-T3 aluminum alloy.

Step 1: Determine the Correct Bend Radius Minimum bend radius charts are found in manufacturers’ maintenance manuals. A radius that is too sharp cracks the material during the bending process. Typically, the drawing indicates the radius to use, but it is a good practice to double check. For this layout example, use the minimum radius chart in Figure 4-124 to choose the correct bend radius for the alloy, temper, and the metal thickness. For 0.040, 2024-T3 the minimum allowable radius is 0.16-inch or 5 ⁄ 32-inch.

Step 2: Find the Setback The setback can be calculated with a formula or can be found in a setback chart available in aircraft maintenance manuals or Source, Maintenance, and Recoverability books (SMRs).

Using a Formula to Calculate the Setback SB = setback K = K-factor (K is 1 for 90° bends) R = inside radius of the bend T = material thickness Since all of the angles in this example are 90° angles, the setback is calculated as follows: SB = K(R+T) = 0.2 inches Note: K = 1 for a 90° bend. For other than a 90° bend, use Using a Setback Chart to Find the Setback The setback chart is a quick way to find the setback and is useful for open and closed bends, because there is no need to calculate or find the K-factor. Several software packages and online calculators are available to calculate the setback. These programs are often used with CAD/CAM programs. • Enter chart at the bottom on the appropriate scale with the sum of the radius and material thickness. • Read up to the bend angle. • Find the setback from corresponding scale on the left.

Example: • Material thickness is 0.063-inch. • Bend angle is 135°. • R + T = 0.183-inch.

Find 0.183 at the bottom of the graph. It is found in the middle scale. • Read up to a bend angle of 135°. • Locate the setback at the left hand side of the graph in the middle scale (0.435-inch).

Step 3: Find the Length of the Flat Line Dimension The flat line dimension can be found using the formula: Flat = MLD – SB MLD = mold line dimension SB = setback The flats, or flat portions of the U-channel, are equal to the mold line dimension minus the setback for each of the sides, and the mold line length minus two setbacks for the center flat. Two setbacks need to be subtracted from the center flat because this flat has a bend on either side.

The flat dimension for the sample U-channel is calculated in the following manner:

Flat dimension = MLD – SB Flat 1 = 1.00-inch – 0.2-inch = 0.8-inch Flat 2 = 2.00-inch – (2 × 0.2-inch) = 1.6-inch Flat 3 = 1.00-inch – 0.2-inch = 0.8-inch Step 4: Find the Bend Allowance When making a bend or fold in a piece of metal, the bend allowance or length of material required for the bend must be calculated. Bend allowance depends on four factors: degree of bend, radius of the bend, thickness of the metal, and type of metal used.

The radius of the bend is generally proportional to the thickness of the material. Furthermore, the sharper the radius of bend, the less the material that is needed for the bend. The type of material is also important. If the material is soft, it can be bent very sharply; but if it is hard, the radius of bend is greater, and the bend allowance is greater. The degree of bend affects the overall length of the metal, whereas the thickness influences the radius of bend.

Bending a piece of metal compresses the material on the inside of the curve and stretches the material on the outside of the curve. However, at some distance between these two extremes lies a space which is not affected by either force. This is known as the neutral line or neutral axis and occurs at a distance approximately 0.445 times the metal thickness (0.445 × T) from the inside of the radius of the bend.

The length of this neutral axis must be determined so that sufficient material can be provided for the bend. This is called the bend allowance. This amount must be added to the overall length of the layout pattern to ensure adequate material for the bend. To save time in calculation of the bend allowance, formulas and charts for various angles, radii of bends, material thicknesses, and other factors have been developed.

Formula 1: Bend Allowance for a 90° Bend To the radius of bend (R) add 1 ⁄ 2 the thickness of the metal (1 ⁄ 2T). This gives R + 1 ⁄ 2T, or the radius of the circle of the neutral axis. Compute the circumference of this circle by multiplying the radius of the neutral line 1 (R + 1 ⁄ 2 T) by 2π ( Note: π = 3.1416): 2π (R + ⁄ 2T). Since a 90° bend is a quarter of the circle, divide the circumference by 4. This gives:

1 2π (R + ⁄ 2T) 4 This is the bend allowance for a 90° bend. To use the formula for a 90° bend having a radius of 1 ⁄ 4 inch for material 0.051-inch thick, substitute in the formula as follows. Bend allowance = (2 × 3.1416)(0.250 + 1 ⁄ 2(0.051)) 4 = 6.2832(0.250 + 0.0255) 4 = 6.2832(0.2755) 4 = 0.4327 The bend allowance, or the length of material required for the bend, is 0.4327 or 7 ⁄ 16-inch. Formula 2: Bend Allowance for a 90° Bend This formula uses two constant values that have evolved over a period of years as being the relationship of the degrees in the bend to the thickness of the metal when determining the bend allowance for a particular application. By experimentation with actual bends in metals, aircraft engineers have found that accurate bending results could be obtained by using the following formula for any degree of bend from 1° to 180°.

Bend allowance = (0.01743R + 0.0078T)N where:

R = the desired bend radius T = the thickness of the metal N = number of degrees of bend To use this formula for a 90° bend having a radius of .16-inch for material 0.040-inch thick, substitute in the formula as follows:

Bend allowance = (0.01743 × 0.16) + (0.0078 × 0.040) × 90 = 0.27 inches Use of Bend Allowance Chart for a 90° Bend In Figure 4-128, the radius of bend is shown on the top line, and the metal thickness is shown on the left hand column. The upper number in each cell is the bend allowance for a 90° bend. The lower number in the cell is the bend allowance per 1° of bend. To determine the bend allowance for a 90° bend, simply use the top number in the chart.

Example: The material thickness of the U-channel is 0.040-inch and the bend radius is 0.16-inch.

Reading across the top of the bend allowance chart, find the column for a radius of bend of .156-inch. Now, find the block in this column that is opposite the material thickness (gauge) of 0.040 in the column at the left. The upper number in the cell is (0.273), the correct bend allowance in inches for a 90° bends.

Several bend allowance calculation programs are available online. Just enter the material thickness, radius, and degree of bend and the computer program calculates the bend allowance.

Use of Chart for Other Than a 90° Bend If the bend is to be other than 90°, use the lower number in the block (the bend allowance for 1°) and compute the bend allowance.

Example: The L-bracket shown in Figure 4-129 is made from 2024-T3 aluminum alloy and the bend is 60° from flat. Note that the bend angle in the figure indicates 120°, but that is the number of degrees between the two flanges and not the bend angle from flat. To find the correct bend angle, use the following formula:

Bend Angle = 180° – Angle between flanges The actual bend is 60°. To find the correct bend radius for a 60° bend of material 0.040-inches thick, use the following procedure.

1. Go to the left side of the table and find 0.040-inch.

2. Go to the right and locate the bend radius of 0.16-inch (0.156-inch).

3. Note the bottom number in the block (0.003034).

4. Multiply this number by the bend angle: 0.003034 × 60 = 0.18204 Step 5: Find the Total Developed Width of the Material The total developed width (TDW) can be calculated when the dimensions of the flats and the bend allowance are found. The following formula is used to calculate TDW:

TDW = Flats + (bend allowance × number of bends)

For the U-channel example, this gives:

TDW = Flat 1 + Flat 2 + Flat 3 + (2 × BA)

TDW = 0.8 + 1.6 + 0.8 + (2 × 0.27)

Note that the amount of metal needed to make the channel is less than the dimensions of the outside of the channel (total of mold line dimensions is 4 inches). This is because the metal follows the radius of the bend rather than going from mold line to mold line. It is good practice to check that the calculated TDW is smaller than the total mold line dimensions. If the calculated TDW is larger than the mold line dimensions, the math was incorrect.

Step 6: Flat Pattern Lay Out After a flat pattern layout of all relevant information is made, the material can be cut to the correct size, and the bend tangent lines can be drawn on the material.

Step 7: Draw the Sight Lines on the Flat Pattern The pattern laid out in Figure 4-130 is complete, except for a sight line that needs to be drawn to help position the bend tangent line directly at the point where the bend should start. Draw a line inside the bend allowance area that is one bend radius away from the bend tangent line that is placed under the brake nose bar. Put the metal in the brake under the clamp and adjust the position of the metal until the sight line is directly below the edge of the radius bar. Now, clamp the brake on the metal and raise the leaf to make the bend. The bend begins exactly on the bend tangent line.

Note: A common mistake is to draw the sight line in the middle of the bend allowance area, instead of one radius away from the bend tangent line that is placed under the brake nose bar.

#### Using a J-Chart to Calculate Total Developed Width

The J-chart, often found in the SRM, can be used to determine bend deduction or setback and the TDW of a flat pattern layout when the inside bend radius, bend angle, and material thickness are known. While not as accurate as the traditional layout method, the J-chart provides sufficient information for most applications. The J-chart does not require difficult calculations or memorized formulas because the required information can be found in the repair drawing or can be measured with simple measuring tools.

When using the J-chart, it is helpful to know whether the angle is open (greater than 90°) or closed (less than 90°) because the lower half of the J-chart is for open angles and the upper half is for closed angles.

To find the total developed width using a J-chart:

• Place a straightedge across the chart and connect the bend radius on the top scale with the material thickness on the bottom scale.

• Locate the angle on the right hand scale and follow this line horizontally until it meets the straight edge. • The factor X (bend deduction) is then read on the diagonally curving line. • Interpolate when the X factor falls between lines. • Add up the mold line dimensions and subtract the X factor to find the TDW.

Example 1 Bend radius = 0.22-inch Material thickness = 0.063-inch Bend angle = 90º ML 1 = 2.00/ML 2 = 2.00 Use a straightedge to connect the bend radius (0.22-inch) at the top of the graph with the material thickness at the bottom (0.063-inch). Locate the 90° angle on the right hand scale and follow this line horizontally until it meets the straightedge. Follow the curved line to the left and find 0.17 at the left side. The X factor in the drawing is 0.17-inch.

Total developed width = (Mold line 1 + Mold line 2) – X factor Total developed width = (2 + 2) – .17 = 3.83-inches Example 2 Bend radius = 0.25-inch Material thickness = 0.050-inch Bend angle = 45º ML 1 = 2.00/ML 2 = 2.00 Figure 4-134 illustrates a 135° angle, but this is the angle between the two legs. The actual bend from flat position is 45° (180 – 135 = 45). Use a straightedge to connect the bend radius (0.25-inch) at the top of the graph with the material thickness at the bottom (.050-inch). Locate the 45° angle on the right hand scale and follow this line horizontally until it meets the straight edge. Follow the curved line to the left and find 0.035 at the left side. The X factor in the drawing is 0.035 inch.

Total developed width = (Mold line 1 + Mold line 2) – X factor Total developed width = (2 + 2) – .035 = 3.965-inch The brake set up for box and pan brakes and cornice brakes is identical. A proper set up of the sheet metal brake is necessary because accurate bending of sheet metal depends on the thickness and temper of the material to be formed and the required radius of the part. Any time a different thickness of sheet metal needs to be formed or when a different radius is required to form the part, the operator needs to adjust the sheet metal brake before the brake is used to form the part. For this example, an L-channel made from 2024 –T3 aluminum alloy that is 0.032-inch thick will be bent.

### Using a Sheet Metal Brake to Fold Metal

#### Step 1: Adjustment of Bend Radius

The bend radius necessary to bend a part can be found in the part drawings, but if it is not mentioned in the drawing, consult the SRM for a minimum bend radius chart. This chart lists the smallest radius allowable for each thickness and temper of metal that is normally used. To bend tighter than this radius would jeopardize the integrity of the part. Stresses left in the area of the bend may cause it to fail while in service, even if it does not crack while bending it.

The brake radius bars of a sheet metal brake can be replaced with another brake radius bar with a different diameter. For example, a 0.032-inch 2024-T3 L channel needs to be bent with a radius of 1 ⁄ 8-inch and a radius bar with a 1 ⁄ 8-inch radius must be installed. If different brake radius bars are not available, and the installed brake radius bar is smaller than required for the part, it is necessary to bend some nose radius shims.

If the radius is so small that it tends to crack annealed aluminum, mild steel is a good choice of material. Experimentation with a small piece of scrap material is necessary to manufacture a thickness that increases the radius to precisely 1 ⁄ 16-inch or 1 ⁄ 8-inch. Use radius and fillet gauges to check this dimension. From this point on, each additional shim is added to the radius before it.

Example: If the original nose was 1 ⁄ 16-inch and a piece of .063-inch material (1 ⁄ 16-inch) was bent around it, the new outside radius is 1 ⁄ 8-inch. If another .063-inch layer (1 ⁄ 16-inch) is added, it is now a 3 ⁄ 16-inch radius. If a piece of .032-inch ( 1 ⁄ 32-inch) instead of .063-inch material ( 1 ⁄ 16-inch) is bent around the 1 ⁄ 8-inch radius, a 5 ⁄ 32-inch radius results.

#### Step 2: Adjusting Clamping Pressure

The next step is setting clamping pressure. Slide a piece of the material with the same thickness as the part to be bent under the brake radius piece. Pull the clamping lever toward the operator to test the pressure. This is an over center type clamp and, when properly set, will not feel springy or spongy when pulled to its fully clamped position. The operator must be able to pull this lever over center with a firm pull and have it bump its limiting stops. On some brakes, this adjustment has to be made on both sides of the brake.

Place test strips on the table 3 inches from each end and one in the center between the bed and the clamp, adjust clamp pressure until it is tight enough to prevent the work pieces from slipping while bending. The clamping pressure can be adjusted with the clamping pressure nut.

#### Step 3: Adjusting the Nose Gap

Adjust the nose gap by turning the large brake nose gap adjustment knobs at the rear of the upper jaw to achieve its proper alignment. The perfect setting is obtained when the bending leaf is held up to the angle of the finished bend and there is one material thickness between the bending leaf and the nose radius piece. Using a piece of material the thickness of the part to be bent as a feeler gauge can help achieve a high degree of accuracy. [Figures 4-140 and 4-141] It is essential this nose gap be perfect, even across the length of the part to be bent. Check by clamping two test strips between the bed and the clamp 3 inches from each end of the brake. Bend 90° , remove test strips, and place one on top of the other; they should match. If they do not match, adjust the end with the sharper bend back slightly.

### Folding a Box

A box can be formed the same way as the U-channel described on in the previous paragraphs, but when a sheet metal part has intersecting bend radii, it is necessary to remove material to make room for the material contained in the flanges. This is done by drilling or punching holes at the intersection of the inside bend tangent lines. These holes, called relief holes and whose diameter is approximately twice the bend radius, relieve stresses in the metal as it is bent and prevent the metal from tearing. Relief holes also provide a neatly trimmed corner from which excess material may be trimmed.

The larger and smoother the relief hole is, the less likely it will be that a crack will form in the corner. Generally, the radius of the relief hole is specified on the drawing. A box and pan brake, also called a finger brake, is used to bend the box. Two opposite sides of the box are bent first. Then, the fingers of the brake are adjusted so the folded-up sides ride up in the cracks between the fingers when the leaf is raised to bend the other two sides.

The size of relief holes varies with thickness of the material. They should be no less than 1 ⁄ 8-inch in diameter for aluminum alloy sheet stock up to and including 0.064-inch thick, or 3 ⁄ 160-inch in diameter for stock ranging from 0.072-inch to 0.128-inch thickness. The most common method of determining the diameter of a relief hole is to use the radius of bend for this dimension, provided it is not less than the minimum allowance (1 ⁄ 8-inch).

#### Relief Hole Location

Relief holes must touch the intersection of the inside bend tangent lines. To allow for possible error in bending, make the relief holes extend 1 ⁄ 32-inch to 1 ⁄ 16-inch behind the inside bend tangent lines. It is good practice to use the intersection of these lines as the center for the holes. The line on the inside of the curve is cut at an angle toward the relief holes to allow for the stretching of the inside flange.

The positioning of the relief hole is important. It should be located so its outer perimeter touches the intersection of the inside bend tangent lines. This keeps any material from interfering with the bend allowance area of the other bend. If these bend allowance areas intersected with each other, there would be substantial compressive stresses that would accumulate in that corner while bending. This could cause the part to crack while bending.

#### Layout Method

Lay out the basic part using traditional layout procedures. This determines the width of the flats and the bend allowance. It is the intersection of the inside bend tangent lines that index the bend relief hole position. Bisect these intersected lines and move outward the distance of the radius of the hole on this line. This is the center of the hole. Drill at this point and finish by trimming off the remainder of the corner material. The trim out is often tangent to the radius and perpendicular to the edge. This leaves an open corner. If the corner must be closed, or a slightly longer flange is necessary, then trim out accordingly. If the corner is to be welded, it is necessary to have touching flanges at the corners. The length of the flange should be one material thickness shorter than the finished length of the part so only the insides of the flanges touch.

### Open & Closed Bends

Open and closed bends present unique problems that require more calculations than 90° bends. In the following 45° and a 135° bend examples, the material is 0.050-inch thick and the bend radius is 3 ⁄ 16-inch.

#### Open End Bend (Less Than 90°)

Figure 4-147 shows an example for a 45° bend. 1. Look up K-factor in K chart. K-factor for 45° is 0.41421-inch. 2. Calculate setback. SB = K(R + T) SB = 0.41421-inch(0.1875-inch + 0.050-inch) = 0.098-inch 3. Calculate bend allowance for 45°. Look up bend allowance for 1° of bend in the bend allowance chart and multiply this by 45. 0.003675-inch × 45 = 0.165-inch 4. Calculate flats. Flat = Mold line dimension – SB Flat 1 = .77-inch – 0.098-inch = 0.672-inch Flat 2 = 1.52-inch – 0.098-inch = 1.422-inch 5. Calculate TDW TDW = Flats + Bend allowance TDW = 0.672-inch + 1.422-inch + 0.165-inch = 2.259-inch.

Observe that the brake reference line is still located one radius from the bend tangent line.

#### Closed End Bend (More Than 90°)

Figure 4-148 shows an example of a 135° bend. 1. Look up K-factor in K chart. K-factor for 135° is 2.4142-inch. 2. Calculate SB. SB = K(R + T) SB = 2.4142-inch(0.1875-inch + 0.050-inch) = 0.57-inch 3. Calculate bend allowance for 135°. Look up bend allowance for 1° of bend in the bend allowance chart and multiply this by 135. 0.003675-inch × 135 = 0.496-inch 4. Calculate flats.

Flat = Mold line dimension – SB Flat 1 = 0.77-inch – 0.57-inch = 0.20-inch Flat 2 = 1.52-inch – 0.57-inch = 0.95-inch TDW = Flats + Bend allowance TDW = 0.20-inch + 0.95-inch + 0.496-inch = 1.65-inch It is obvious from both examples that a closed bend has a smaller TDW than an open-end bend and the material length needs to be adjusted accordingly.

### Hand Forming

All hand forming revolves around the processes of stretching and shrinking metal. As discussed earlier, stretching means to lengthen or increase a particular area of metal while shrinking means to reduce an area. Several methods of stretching and shrinking may be used, depending on the size, shape, and contour of the part being formed.

For example, if a formed or extruded angle is to be curved, either stretch one leg or shrink the other, whichever makes the part fit. In bumping, the material is stretched in the bulge to make it balloon, and in joggling, the material is stretched between the joggles. Material in the edge of lightening holes is often stretched to form a beveled reinforcing ridge around them. The following paragraphs discuss some of these techniques.

#### Straight Line Bends

The cornice brake and bar folder are ordinarily used to make straight bends. Whenever such machines are not available, comparatively short sections can be bent by hand with the aid of wooden or metal bending blocks.

After a blank has been laid out and cut to size, clamp it along the bend line between two wooden forming blocks held in a vise. The wooden forming blocks should have one edge rounded as needed for the desired radius of bend. It should also be curved slightly beyond 90° to allow for spring-back.

Bend the metal that protrudes beyond the bending block to the desired angle by tapping lightly with a rubber, plastic, or rawhide mallet. Start tapping at one end and work back and forth along the edge to make a gradual and even bend. Continue this process until the protruding metal is bent to the desired angle against the forming block. Allow for spring-back by driving the material slightly farther than the actual bend. If a large amount of metal extends beyond the forming blocks, maintain hand pressure against the protruding sheet to prevent it from bouncing. Remove any irregularities by holding a straight block of hardwood edgewise against the bend and striking it with heavy blows of a mallet or hammer. If the amount of metal protruding beyond the bending blocks is small, make the entire bend by using the hardwood block and hammer.

#### Formed or Extruded Angles

Both formed and extruded types of angles can be curved (not bent sharply) by stretching or shrinking either of the flanges. Curving by stretching one flange is usually preferred since the process requires only a V-block and a mallet and is easily accomplished.

Stretching with V-Block Method In the stretching method, place the flange to be stretched in the groove of the V-block. (If the flange is to be shrunk, place the flange across the V-block.) Using a round, soft-faced mallet, strike the flange directly over the V portion with light, even blows while gradually forcing it downward into the V .

Begin at one end of the flange and form the curve gradually and evenly by moving the strip slowly back and forth, distributing the hammer blows at equal spaces on the flange. Hold the strip firmly to keep it from bouncing when hammered. An overly heavy blow buckles the metal, so keep moving the flange across the V-block, but always lightly strike the spot directly above the V .

Lay out a full-sized, accurate pattern on a sheet of paper or plywood and periodically check the accuracy of the curve. Comparing the angle with the pattern determines exactly how the curve is progressing and just where it needs to be increased or decreased. It is better to get the curve to conform roughly to the desired shape before attempting to finish any one portion, because the finishing or smoothing of the angle may cause some other portion of the angle to change shape. If any part of the angle strip is curved too much, reduce the curve by reversing the angle strip on the V-block, placing the bottom flange up, and striking it with light blows of the mallet.

Try to form the curve with a minimum amount of hammering, for excessive hammering work hardens the metal. Work-hardening can be recognized by a lack of bending response or by springiness in the metal. It can be recognized very readily by an experienced worker. In some cases, the part may have to be annealed during the curving operation. If so, be sure to heat treat the part again before installing it on the aircraft.

Shrinking With V-Block & Shrinking Block Methods Curving an extruded or formed angle strip by shrinking may be accomplished by either the previously discussed V-block method or the shrinking block method. While the V-block is more satisfactory because it is faster, easier, and affects the metal less, good results can be obtained by the shrinking block method.

In the V-block method, place one flange of the angle strip flat on the V-block with the other flange extending upward. Using the process outlined in the stretching paragraphs, begin at one end of the angle strip and work back and forth making light blows. Strike the edge of the flange at a slight angle to keep the vertical flange from bending outward.

Occasionally, check the curve for accuracy with the pattern. If a sharp curve is made, the angle (cross-section of the formed angle) closes slightly. To avoid such closing of the angle, clamp the angle strip to a hardwood board with the hammered flange facing upward using small C-clamps. The jaws of the C-clamps should be covered with masking tape. If the angle has already closed, bring the flange back to the correct angle with a few blows of a mallet or with the aid of a small hardwood block. If any portion of the angle strip is curved too much, reduce it by reversing the angle on the V-block and hammering with a suitable mallet, as explained in the previous paragraph on stretching. After obtaining the proper curve, smooth the entire angle by planishing with a soft-faced mallet.

If the curve in a formed angle is to be quite sharp or if the flanges of the angle are rather broad, the shrinking block method is generally used. In this process, crimp the flange that is to form the inside of the curve.

When making a crimp, hold the crimping pliers so that the jaws are about 1 ⁄ 8-inch apart. By rotating the wrist back and forth, bring the upper jaw of the pliers into contact with the flange, first on one side and then on the other side of the lower jaw. Complete the crimp by working a raised portion into the flange, gradually increasing the twisting motion of the pliers. Do not make the crimp too large because it will be difficult to work out. The size of the crimp depends upon the thickness and softness of the material, but usually about 1 ⁄ 4-inch is sufficient. Place several crimps spaced evenly along the desired curve with enough space left between each crimp so that jaws of the shrinking block can easily be attached.

After completing the crimping, place the crimped flange in the shrinking block so that one crimp at a time is located between the jaws. Flatten each crimp with light blows of a soft-faced mallet, starting at the apex (the closed end) of the crimp and gradually working toward the edge of the flange. Check the curve of the angle with the pattern periodically during the forming process and again after all the crimps have been worked out. If it is necessary to increase the curve, add more crimps and repeat the process. Space the additional crimps between the original ones so that the metal does not become unduly work hardened at any one point. If the curve needs to be increased or decreased slightly at any point, use the V-block.

After obtaining the desired curve, planish the angle strip over a stake or a wooden form.

#### Flanged Angles

The forming process for the following two flanged angles is slightly more complicated than the previously discussed angles because the bend is shorter (not gradually curved) and necessitates shrinking or stretching in a small or concentrated area. If the flange is to point toward the inside of the bend, the material must be shrunk. If it is to point toward the outside, it must be stretched.

#### Shrinking

In forming a flanged angle by shrinking, use wooden forming blocks similar to those shown in Figure 4-151 and proceed as follows:

1. Cut the metal to size, allowing for trimming after forming. Determine the bend allowance for a 90° bend and round the edge of the forming block accordingly.

2. Clamp the material in the form blocks as shown in Figure 4-151, and bend the exposed flange against the block. After bending, tap the blocks slightly. This induces a setting process in the bend.

3. Using a soft-faced shrinking mallet, start hammering near the center and work the flange down gradually toward both ends. The flange tends to buckle at the bend because the material is made to occupy less space. Work the material into several small buckles instead of one large one and work each buckle out gradually by hammering lightly and gradually compressing the material in each buckle. The use of a small hardwood wedge block aids in working out the buckles.

4. Planish the flange after it is flattened against the form block and remove small irregularities. If the form blocks are made of hardwood, use a metal planishing hammer. If the forms are made of metal, use a soft-faced mallet. Trim the excess material away and file and polish.

#### Stretching

To form a flanged angle by stretching, use the same forming blocks, wooden wedge block, and mallet as used in the shrinking process and proceed as follows:

1. Cut the material to size (allowing for trim), determine bend allowance for a 90° bend, and round off the edge of the block to conform to the desired radius of bend.

2. Clamp the material in the form blocks.

3. Using a soft-faced stretching mallet, start hammering near the ends and work the flange down smoothly and gradually to prevent cracking and splitting. Planish the flange and angle as described in the previous procedure, and trim and smooth the edges, if necessary.

#### Curved Flanged Parts

Curved flanged parts are usually hand formed with a concave flange, the inside edge, and a convex flange, the outside edge. The concave flange is formed by stretching, while the convex flange is formed by shrinking. Such parts are shaped with the aid of hardwood or metal forming blocks. These blocks are made in pairs and are designed specifically for the shape of the area being formed. These blocks are made in pairs similar to those used for straight angle bends and are identified in the same manner. They differ in that they are made specifically for the particular part to be formed, they fit each other exactly, and they conform to the actual dimensions and contour of the finished article.

The forming blocks may be equipped with small aligning pins to help line up the blocks and to hold the metal in place or they may be held together by C-clamps or a vise. They also may be held together with bolts by drilling through form blocks and the metal, provided the holes do not affect the strength of the finished part. The edges of the forming block are rounded to give the correct radius of bend to the part, and are undercut approximately 5° to allow for spring-back of the metal. This undercut is especially important if the material is hard or if the bend must be accurate.

The nose rib offers a good example of forming a curved flange because it incorporates both stretching and shrinking (by crimping). They usually have a concave flange, the inside edge, and a convex flange, the outside edge. Note the various types of forming represented in the following figures. In the plain nose rib, only one large convex flange is used. Because of the great distance around the part and the likelihood of buckles in forming, it is rather difficult to form. The flange and the beaded (raised ridge on sheet metal used to stiffen the piece) portion of this rib provide sufficient strength to make this a good type to use. In Figure 4-156 , the concave flange is difficult to form, but the outside flange is broken up into smaller sections by relief holes. In Figure 4-157 , note that crimps are placed at equally spaced intervals to absorb material and cause curving, while also giving strength to the part.

In Figure 4-158 , the nose rib is formed by crimping, beading, putting in relief holes, and using a formed angle riveted on each end. The beads and the formed angles supply strength to the part. The basic steps in forming a curved flange follow: [Figures 4-159 and 160]

1. Cut the material to size, allowing about 1 ⁄ 4-inch excess material for trim and drill holes for alignment pins.

2. Remove all burrs (jagged edges). This reduces the possibility of the material cracking at the edges during the forming process.

3. Locate and drill holes for alignment pins. 4. Place the material between the form blocks and clamp blocks tightly in a vise to prevent the material from moving or shifting. Clamp the work as closely as possible to the particular area being hammered to prevent strain on the form blocks and to keep the metal from slipping.

Concave Surfaces Bend the flange on the concave curve first. This practice may keep the flange from splitting open or cracking when the metal is stretched. Should this occur, a new piece must be made. Using a plastic or rawhide mallet with a smooth, slightly rounded face, start hammering at the extreme ends of the part and continue toward the center of the bend. This procedure permits some of the metal at the ends of the part to be worked into the center of the curve where it is needed. Continue hammering until the metal is gradually worked down over the entire flange, flush with the form block. After the flange is formed, trim off the excess material and check the part for accuracy.

Convex Surfaces Convex surfaces are formed by shrinking the material over a form block. Using a wooden or plastic shrinking mallet and a backup or wedge block, start at the center of the curve and work toward both ends. Hammer the flange down over the form, striking the metal with glancing blows at an angle of approximately 45° and with a motion that tends to pull the part away from the radius of the form block. Stretch the metal around the radius bend and remove the buckles gradually by hammering on a wedge block. Use the backup block to keep the edge of the flange as nearly perpendicular to the form block as possible. The backup block also lessens the possibility of buckles, splits, or cracks. Finally, trim the flanges of excess metal, planish, remove burrs, round the corners (if any), and check the part for accuracy.

#### Forming by Bumping

As discussed earlier, bumping involves stretching the sheet metal by bumping it into a form and making it balloon. Bumping can be done on a form block or female die, or on a sandbag.

Either method requires only one form: a wooden block, a lead die, or a sandbag. The blister, or streamlined cover plate, is an example of a part made by the form block or die method of bumping. Wing fillets are an example of parts that are usually formed by bumping on a sandbag.

Form Block or Die The wooden block or lead die designed for form block bumping must have the same dimensions and contour as the outside of the blister. To provide enough bucking weight and bearing surface for fastening the metal, the block or die should be at least one inch larger in all dimensions than the form requires. Follow these procedures to create a form block: 1. Hollow the block out with tools, such as saws, chisels, gouges, files, and rasps.

2. Smooth and finish the block with sandpaper. The inside of the form must be as smooth as possible, because the slightest irregularity shows up on the finished part.

3. Prepare several templates (patterns of the cross-section), as shown in Figure 4-161 so that the form can be checked for accuracy.

4. Shape the contour of the form at points 1, 2, and 3.

5. Shape the areas between the template checkpoints to conform the remaining contour to template 4. Shaping of the form block requires particular care because the more nearly accurate it is, the less time it takes to produce a smooth, finished part.

After the form is prepared and checked, perform the bumping as follows:

1. Cut a metal blank to size allowing an extra 1 ⁄ 2 to 1-inch to permit drawing.

2. Apply a thin coat of light oil to the block and the aluminum to prevent galling (scraping on rough spots).

3. Clamp the material between the block and steel plate. Ensure it is firmly supported yet it can slip a little toward the inside of the form.

4. Clamp the bumping block in a bench vise. Use a soft-faced rubber mallet, or a hardwood drive block with a suitable mallet, to start the bumping near the edges of the form.

5. Work the material down gradually from the edges with light blows of the mallet. Remember, the purpose of bumping is to work the material into shape by stretching rather than forcing it into the form with heavy blows. Always start bumping near the edge of the form. Never start near the center of the blister.

6. Before removing the work from the form, smooth it as much as possible by rubbing it with the rounded end of either a maple block or a stretching mallet.

7. Remove the blister from the bumping block and trim to size.

Sandbag Bumping Sandbag bumping is one of the most difficult methods of hand forming sheet metal because there is no exact forming block to guide the operation. In this method, a depression is made into the sandbag to take the shape of the hammered portion of the metal. The depression or pit has a tendency to shift from the hammering, which necessitates periodic readjustment during the bumping process. The degree of shifting depends largely on the contour or shape of the piece being formed, and whether glancing blows must be struck to stretch, draw, or shrink the metal. When forming by this method, prepare a contour template or some sort of a pattern to serve as a working guide and to ensure accuracy of the finished part. Make the pattern from ordinary kraft or similar paper, folding it over the part to be duplicated. Cut the paper cover at the points where it would have to be stretched to fit, and attach additional pieces of paper with masking tape to cover the exposed portions. After completely covering the part, trim the pattern to exact size.

Open the pattern and spread it out on the metal from which the part is to be formed. Although the pattern does not lie flat, it gives a fairly accurate idea of the approximate shape of the metal to be cut, and the pieced-in sections indicate where the metal is to be stretched. When the pattern has been placed on the material, outline the part and the portions to be stretched using a felt-tipped pen. Add at least one inch of excess metal when cutting the material to size. Trim off the excess metal after bumping the part into shape.

If the part to be formed is radially symmetrical, it is fairly easy to shape since a simple contour template can be used as a working guide. The procedure for bumping sheet metal parts on a sandbag follows certain basic steps that can be applied to any part, regardless of its contour or shape.

1. Lay out and cut the contour template to serve as a working guide and to ensure accuracy of the finished part. (This can be made of sheet metal, medium to heavy cardboard, kraft paper, or thin plywood.)

2. Determine the amount of metal needed, lay it out, and cut it to size, allowing at least 1 ⁄ 2-inch in excess.

3. Place a sandbag on a solid foundation capable of supporting heavy blows and make a pit in the bag with a smooth-faced mallet. Analyze the part to determine the correct radius the pit should have for the forming operation. The pit changes shape with the hammering it receives and must be readjusted accordingly.

4. Select a soft round-faced or bell-shaped mallet with a contour slightly smaller than the contour desired on the sheet metal part. Hold one edge of the metal in the left hand and place the portion to be bumped near the edge of the pit on the sandbag. Strike the metal with light glancing blows.

5. Continue bumping toward the center, revolving the metal, and working gradually inward until the desired shape is obtained. Shape the entire part as a unit.

6. Check the part often for accuracy of shape during the bumping process by applying the template. If wrinkles form, work them out before they become too large.

7. Remove small dents and hammer marks with a suitable stake and planishing hammer or with a hand dolly and planishing hammer.

8. Finally, after bumping is completed, use a pair of dividers to mark around the outside of the object. Trim the edge and file it smooth. Clean and polish the part.

#### Joggling

A joggle, often found at the intersection of stringers and formers, is the offset formed on a part to allow clearance for a sheet or another mating part. Use of the joggle maintains the smooth surface of a joint or splice. The amount of offset is usually small; therefore, the depth of the joggle is generally specified in thousandths of an inch. The thickness of the material to be cleared governs the depth of the joggle. In determining the necessary length of the joggle, allow an extra 1 ⁄ 16-inch to give enough added clearance to assure a fit between the joggled, overlapped part. The distance between the two bends of a joggle is called the allowance. This dimension is normally called out on the drawing. However, a general rule of thumb for figuring allowance is four times the thickness of the displacement of flat sheets. For 90° angles, it must be slightly more due to the stress built up at the radius while joggling. For extrusions, the allowance can be as much as 12 times the material thickness, so, it is important to follow the drawing.

There are a number of different methods of forming joggles. For example, if the joggle is to be made on a straight flange or flat piece of metal, it can be formed on a cornice brake. To form the joggle, use the following procedure:

1. Lay out the boundary lines of the joggle where the bends are to occur on the sheet.

2. Insert the sheet in the brake and bend the metal up approximately 20° to 30°.

3. Release the brake and remove the part.

4. Turn the part over and clamp it in the brake at the second bend line.

5. Bend the part up until the correct height of the joggle is attained.

6. Remove the part from the brake and check the joggle for correct dimensions and clearance.

When a joggle is necessary on a curved part or a curved flange, forming blocks or dies made of hardwood, steel, or aluminum alloy may be used. The forming procedure consists of placing the part to be joggled between the two joggle blocks and squeezing them in a vice or some other suitable clamping device. After the joggle is formed, the joggle blocks are turned over in the vice and the bulge on the opposite flange is flattened with a wooden or rawhide mallet.

Since hardwood is easily worked, dies made of hardwood are satisfactory when the die is to be used only a few times. If a number of similar joggles are to be produced, use steel or aluminum alloy dies. Dies of aluminum alloy are preferred since they are easier to fabricate than those of steel and wear about as long. These dies are sufficiently soft and resilient to permit forming aluminum alloy parts on them without marring, and nicks and scratches are easily removed from their surfaces.

When using joggling dies for the first time, test them for accuracy on a piece of waste stock to avoid the possibility of ruining already fabricated parts. Always keep the surfaces of the blocks free from dirt, filings, and the like, so that the work is not marred.

#### Lightening Holes

Lightening holes are cut in rib sections, fuselage frames, and other structural parts to decrease weight. To avoid weakening the member by removal of the material, flanges are often pressed around the holes to strengthen the area from which the material was removed.

Lightening holes should never be cut in any structural part unless authorized. The size of the lightening hole and the width of the flange formed around the hole are determined by design specifications. Margins of safety are considered in the specifications so that the weight of the part can be decreased and still retain the necessary strength. Lightening holes may be cut with a hole saw, a punch, or a fly cutter. The edges are filed smooth to prevent them from cracking or tearing.

Flanging Lightening Holes Form the flange by using a flanging die, or hardwood or metal form blocks. Flanging dies consist of two matching parts: a female and a male die. For flanging soft metal, dies can be of hardwood, such as maple. For hard metal or for more permanent use, they should be made of steel. The pilot guide should be the same size as the hole to be flanged, and the shoulder should be the same width and angle as the desired flange.

When flanging lightening holes, place the material between the mating parts of the die and form it by hammering or squeezing the dies together in a vise or in an arbor press (a small hand operated press). The dies work more smoothly if they are coated with light machine oil.

### Working Stainless Steel

Corrosion-resistant-steel (CRES) sheet is used on some parts of the aircraft when high strength is required. CRES causes magnesium, aluminum, or cadmium to corrode when it touches these metals. To isolate CRES from magnesium and aluminum, apply a finish that gives protection between their mating surfaces. It is important to use a bend radius that is larger than the recommended minimum bend radius to prevent cracking of the material in the bend area.

When working with stainless steel, make sure that the metal does not become unduly scratched or marred. Also, take special precautions when shearing, punching, or drilling this metal. It takes about twice as much pressure to shear or punch stainless steel as it does mild steel. Keep the shear or punch and die adjusted very closely. Too much clearance permits the metal to be drawn over the edge of the die and causes it to become work hardened, resulting in excessive strain on the machine. When drilling stainless steel, use an HSS drill bit ground to an included angle of 135°. Keep the drill speed about one-half that required for drilling mild steel, but never exceed 750 rpm. Keep a uniform pressure on the drill so the feed is constant at all times. Drill the material on a backing plate, such as cast iron, which is hard enough to permit the drill bit to cut completely through the stock without pushing the metal away from the drill point. Spot the drill bit before turning on the power and also make sure that pressure is exerted when the power is turned on.

### Working Inconel® Alloys 625 & 718

Inconel® refers to a family of nickel-chromium-iron super alloys typically used in high-temperature applications. Corrosion resistance and the ability to stay strong in high temperatures led to the frequent use of these Inconel® alloys in aircraft powerplant structures. Inconel® alloys 625 and 718 can be cold formed by standard procedures used for steel and stainless steel.

Normal drilling into Inconel ® alloys can break drill bits sooner and cause damage to the edge of the hole when the drill bit goes through the metal. If a hand drill is used to drill Inconel® alloys 625 and 718, select a 135° cobalt drill bit. When hand drilling, push hard on the drill, but stay at a constant chip rate. For example, with a No. 30 hole, push the drill with approximately 50 pounds of force. Use the maximum drill rpm as illustrated in Figure 4-166 . A cutting fluid is not necessary when hand drilling.

The following drilling procedures are recommended:

• Drill pilot holes in loose repair parts with power feed equipment before preassembling them.

• Preassemble the repair parts and drill the pilot holes in the mating structure.

• Enlarge the pilot holes to their completed hole dimension.

When drilling Inconel ®, autofeed-type drilling equipment is preferred.

### Working Magnesium

Warning: Keep magnesium particles away from sources of ignition. Small particles of magnesium burn very easily. In sufficient concentration, these small particles can cause an explosion. If water touches molten magnesium, a steam explosion could occur. Extinguish magnesium fires with dry talc, calcium carbonate, sand, or graphite. Apply the powder on the burning metal to a depth of 1 ⁄ 2-inch or more. Do not use foam, water, carbon tetrachloride, or carbon dioxide. Magnesium alloys must not touch methyl alcohol.

Magnesium is the world’s lightest structural metal. Like many other metals, this silvery-white element is not used in its pure state for stressed application. Instead, magnesium is alloyed with certain other metals (aluminum, zinc, zirconium, manganese, thorium, and rare earth metals) to obtain the strong, lightweight alloys needed for structural uses. When alloyed with these other metals, magnesium, yields alloys with excellent properties and high strength- to-weight ratios. Proper combination of these alloying constituents provide alloys suitable for sand, permanent mold and die castings, forging, extrusions, rolled sheet, and plate with good properties at room temperature, as well as at elevated temperatures.

Lightweight is the best known characteristic of magnesium, an important factor in aircraft design. In comparison, aluminum weighs one and one half times more, iron and steel weigh four times more, and copper and nickel alloys weigh five times more. Magnesium alloys can be cut, drilled, and reamed with the same tools that are used on steel or brass, but the cutting edges of the tool must be sharp. Type B rivets (5056-F aluminum alloy) are used when riveting magnesium alloy parts. Magnesium parts are often repaired with clad 2024-T3 aluminum alloy.

While magnesium alloys can usually be fabricated by methods similar to those used on other metals, remember that many of the details of shop practice cannot be applied. Magnesium alloys are difficult to fabricate at room temperature; therefore, most operations must be performed at high temperatures. This requires preheating of the metal or dies, or both. Magnesium alloy sheets may be cut by blade shears, blanking dies, routers, or saws. Hand or circular saws are usually used for cutting extrusions to length. Conventional shears and nibblers should never be used for cutting magnesium alloy sheet because they produce a rough, cracked edge.

Shearing and blanking of magnesium alloys require close tool tolerances. A maximum clearance of 3 to 5 percent of the sheet thickness is recommended. The top blade of the shears should be ground with an included angle of 45° to 60º. The shear angle on a punch should be from 2° to 3°, with a 1° clearance angle on the die. For blanking, the shear angle on the die should be from 2° to 3° with a 1° clearance angle on the punch. Hold-down pressures should be used when possible. Cold shearing should not be accomplished on a hard-rolled sheet thicker than 0.064-inch or annealed sheet thicker than 1 ⁄ 8-inch. Shaving is used to smooth the rough, flaky edges of a magnesium sheet that has been sheared. This operation consists of removing approximately 1 ⁄ 32-inch by a second shearing.

Hot shearing is sometimes used to obtain an improved sheared edge. This is necessary for heavy sheet and plate stock. Annealed sheet may be heated to 600 °F, but hard-rolled sheet must be held under 400 °F, depending on the alloy used. Thermal expansion makes it necessary to allow for shrinkage after cooling, which entails adding a small amount of material to the cold metal dimensions before fabrication.

Sawing is the only method used in cutting plate stock more than 1 ⁄ 2-inch thick. Bandsaw raker-set blades of 4-to 6-tooth pitch are recommended for cutting plate stock or heavy extrusions. Small and medium extrusions are more easily cut on a circular cutoff saw having six teeth per inch. Sheet stock can be cut on handsaws having raker-set or straight-set teeth with an 8-tooth pitch. Bandsaws should be equipped with nonsparking blade guides to eliminate the danger of sparks igniting the magnesium alloy filings.

Cold working most magnesium alloys at room temperature is very limited, because they work harden rapidly and do not lend themselves to any severe cold forming. Some simple bending operations may be performed on sheet material, but the radius of bend must be at least 7 times the thickness of the sheet for soft material and 12 times the thickness of the sheet for hard material. A radius of 2 or 3 times the thickness of the sheet can be used if the material is heated for the forming operation.

Since wrought magnesium alloys tend to crack after they are cold-worked, the best results are obtained if the metal is heated to 450 °F before any forming operations are attempted. Parts formed at the lower temperature range are stronger because the higher temperature range has an annealing effect on the metal.

The disadvantages of hot working magnesium are:

1. Heating the dies and the material is expensive and troublesome.

2. There are problems in lubricating and handling materials at these temperatures.

The advantages to hot working magnesium are:

1. It is more easily formed when hot than are other metals.

2. Spring-back is reduced, resulting in greater dimensional accuracy.

When heating magnesium and its alloys, watch the temperature carefully as the metal is easily burned. Overheating also causes small molten pools to form within the metal. In either case, the metal is ruined. To prevent burning, magnesium must be protected with a sulfur dioxide atmosphere while being heated.

Proper bending around a short radius requires the removal of sharp corners and burrs near the bend line. Layouts should be made with a carpenter’s soft pencil because any marring of the surface may result in fatigue cracks.

Press brakes can be used for making bends with short radii. Die and rubber methods should be used where bends are to be made at right angles, which complicate the use of a brake. Roll forming may be accomplished cold on equipment designed for forming aluminum. The most common method of forming and shallow drawing of magnesium is to use a rubber pad as the female die. This rubber pad is held in an inverted steel pan that is lowered by a hydraulic press ram. The press exerts pressure on the metal and bends it to the shape of the male die.

The machining characteristics of magnesium alloys are excellent, making possible the use of maximum speeds of the machine tools with heavy cuts and high feed rates. Power requirements for machining magnesium alloys are about one-sixth of those for mild steel.

Filings, shavings, and chips from machining operations should be kept in covered metal containers because of the danger of combustion. Do not use magnesium alloys in liquid deicing and water injection systems or in the integral fuel tank areas.

### Working Titanium

Keep titanium particles away from sources of ignition. Small particles of titanium burn very easily. In sufficient concentration, these small particles can cause an explosion. If water touches molten titanium, a steam explosion could occur. Extinguish titanium fires with dry talc, calcium carbonate, sand, or graphite. Apply the powder on the burning metal to a depth of 1 ⁄ 2-inch or more. Do not use foam, water, carbon tetrachloride, or carbon dioxide.

#### Description of Titanium

Titanium in its mineral state, is the fourth most abundant structural metal in the earth’s crust. It is lightweight, nonmagnetic, strong, corrosion resistant, and ductile. Titanium lies between the aluminum alloys and stainless steel in modulus, density, and strength at intermediate temperatures. Titanium is 30 percent stronger than steel, but is nearly 50 percent lighter. It is 60 percent heavier than aluminum, but twice as strong.

Titanium and its alloys are used chiefly for parts that require good corrosion resistance, moderate strength up to 600 °F (315 °C), and lightweight. Commercially pure titanium sheet may be formed by hydropress, stretch press, brake roll forming, drop hammer, or other similar operations. It is more difficult to form than annealed stainless steel. Titanium can also be worked by grinding, drilling, sawing, and the types of working used on other metals. Titanium must be isolated from magnesium, aluminum, or alloy steel because galvanic corrosion or oxidation of the other metals occurs upon contact.

Monel® rivets or standard close-tolerance steel fasteners should be used when installing titanium parts. The alloy sheet can be formed, to a limited extent, at room temperature. The forming of titanium alloys is divided into three classes:

• Cold forming with no stress relief • Cold forming with stress relief • Elevated temperature forming (built-in stress relief)

Over 5 percent of all titanium in the United States is produced in the form of the alloy Ti 6Al-4V , which is known as the workhorse of the titanium industry. Used in aircraft turbine engine components and aircraft structural components, Ti 6Al-4V is approximately 3 times stronger than pure titanium. The most widely used titanium alloy, it is hard to form.

The following are procedures for cold forming titanium 6Al-4V annealed with stress relief (room temperature forming):

1. It is important to use a minimum radius chart when forming titanium because an excessively small radius introduces excess stress to the bend area.

2. Stress relieves the part as follows: heat the part to a temperature above 1,250 °F (677 °C), but below 1,450 °F (788 °C). Keep the part at this temperature for more than 30 minutes but less than 10 hours.

3. A powerful press brake is required to form titanium parts. Regular hand-operated box and pan brakes cannot form titanium sheet material.

4. A power slip roller is often used if the repair patch needs to be curved to fit the contour of the aircraft.

Titanium can be difficult to drill, but standard high-speed drill bits may be used if the bits are sharp, if sufficient force is applied, and if a low-speed drill motor is used. If the drill bit is dull, or if it is allowed to ride in a partially drilled hole, an overheated condition is created, making further drilling extremely difficult. Therefore, keep holes as shallow as possible; use short, sharp drill bits of approved design; and flood the area with large amounts of cutting fluid to facilitate drilling or reaming.

When working titanium, it is recommended that you use carbide or 8 percent cobalt drill bits, reamers, and countersinks. Ensure the drill or reamer is rotating to prevent scoring the side of the hole when removing either of them from a hole. Use a hand drill only when positive-power-feed drills are not available.

The following guidelines are used for drilling titanium:

• The largest diameter hole that can be drilled in a single step is 0.1563-inch because a large force is required.

Larger diameter drill bits do not cut satisfactorily when much force is used. Drill bits that do not cut satisfactorily cause damage to the hole.

• Holes with a diameter of 0.1875-inch and larger can be hand drilled if the operator:

- Starts with a hole with a diameter of 0.1563-inch.

- Increases the diameter of the hole in 0.0313-inch or 0.0625-inch increments.

• Cobalt vanadium drill bits last much longer than HSS bits.

• The recommended drill motor rpm settings for hand drilling titanium are listed in Figure 4-167 .

• The life of a drill bit is shorter when drilling titanium than when drilling steel. Do not use a blunt drill bit or let a drill bit rub the surface of the metal and not cut it. If one of these conditions occurs, the titanium surface becomes work hardened, and it is very difficult to start the drill again.

• When hand drilling two or more titanium parts at the same time, clamp them together tightly. To clamp them together, use temporary bolts, Cleco clamps, or tooling clamps. Put the clamps around the area to drill and as near the area as possible.

• When hand drilling thin or flexible parts, put a support (such as a block of wood) behind the part.

• Titanium has a low thermal conductivity. When it becomes hot, other metals become easily attached to it. Particles of titanium often become welded to the sharp edges of the drill bit if the drill speed is too high. When drilling large plates or extrusions, use a water soluble coolant or sulphurized oil.

Note: The intimate metal-to-metal contact in the metal working process creates heat and friction that must be reduced or the tools and the sheet metal used in the process are quickly damaged and/or destroyed. Coolants, also called cutting fluids, are used to reduce the friction at the interface of the tool and sheet metal by transferring heat away from the tool and sheet metal. Thus, the use of cutting fluids increases productivity, extends tool life, and results in a higher quality of workmanship.

## 2. 中文翻译

TODO

## 3. 专业词汇

| 英文 | 词性 | 中文 | 本节语境 |
| --- | --- | --- | --- |
TODO

## 4. 语法解析

TODO
