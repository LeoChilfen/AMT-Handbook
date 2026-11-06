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

### 术语

下列术语常用于钣金成形与展开图（flat pattern）放样。熟悉这些术语有助于理解弯曲计算在折弯作业中是如何使用的。图 4-120 示出了其中大部分术语。

基准尺寸（Base measurement）——成形件的外部尺寸。基准尺寸标注在图纸或蓝图上，也可从原零件上量取。

长边（Leg）——成形角材中较长的一边。

折边（Flange）——成形角材中较短的一边，与长边相对。若角材两边等长，则两边都称为长边。

金属纹理（Grain of the metal）——板材由熔融铸锭轧制而成时形成的材料天然纹理。若条件允许，折弯线应与金属纹理成 90° 角。

弯曲余量（Bend allowance，BA）——指弯曲处内部那段呈弧形的金属（即折弯时被弯曲的那部分金属）。弯曲余量可视为中性线弧形段的长度。

弯曲半径（Bend radius）——板材折弯时形成圆弧，此圆弧的半径称为弯曲半径。弯曲半径由圆心量至金属内表面。最小弯曲半径取决于材料的回火状态、厚度和种类。务必使用《最小弯曲半径表》确定所用合金的最小弯曲半径。最小弯曲半径图表可在制造厂维护手册中查到。

折弯切线（Bend tangent line，BL）——金属开始弯曲的位置，也是金属结束弯曲的线。两条折弯切线之间的全部空间即为弯曲余量。

中性轴（Neutral axis）——一条假想线，弯曲后的长度与弯曲前相同。弯曲后，弯曲区比弯曲前减薄 10%～15%。弯曲区的这种减薄使金属的中性线向圆心方向移动。为便于计算，常假定中性轴位于材料厚度的中央，尽管中性轴并不正好在材料中央。不过由此产生的误差极小，对大多数工作而言，假定其在中央是足够准确的。

模线（Mold line，ML）——零件平直边越过圆角向外延伸的线。

模线尺寸（Mold line dimension，MLD）——由模线相交得出的零件尺寸，即零件若没有圆角时所具有的尺寸。

模点（Mold point）——模线的交点。若零件没有圆角，模点就是其外角。

K 系数（K-Factor）——材料厚度中不发生拉伸或压缩的那一部分所占的百分比，例如中性轴所在位置。该百分比已经过计算，是 K 图表上 179 个数之一，对应金属可弯曲的 0° 至 180° 之间的某个角度。凡需将金属弯成 90° 以外的任何角度（90° 的 K 系数等于 1）时，都从图表中选取相应的 K 系数值，再乘以金属的半径（R）与厚度（T）之和。乘积即为该弯的退让量（setback，见下一段）。如果没有 K 图表，可用计算器按下列公式计算 K 系数：K 值等于弯曲角一半的正切。

退让量（Setback，SB）——折弯机的夹口必须自模线后退的距离，以便成形弯边。对 90° 弯，SB = R + T（弯曲半径加金属厚度）。退让量必须在折弯之前确定，因为它用于确定起始折弯切线的位置。零件若不止一处弯，每一处弯都要减去相应的退让量。钣金中的大多数弯是 90° 弯；凡小于或大于 90° 的弯都必须使用 K 系数。

对准线（Sight line）——又称折弯线或折弯机线，是待成形金属上的一条放样线，与折弯机鼻梁对齐，在折弯工件时起导向作用。

平直段（Flat）——零件上不属于弯曲的那一部分。它等于基准尺寸（MLD）减去退让量。平直段 = MLD – SB 闭合角（Closed angle）——两长边之间量得小于 90°，或按弯曲量量得大于 90° 的角。

开口角（Open angle）——两长边之间量得大于 90°，或按弯曲量量得小于 90° 的角。

总展开宽度（Total developed width，TDW）——绕过各弯、自一边量至另一边的材料宽度。求 TDW 是确定下料尺寸所必需的。TDW 小于各模线尺寸之和，因为金属是沿圆弧弯曲的，而不是像模线尺寸所表示的那样折成方角。

### 放样或展开图绘制

为防止材料浪费并使成品零件获得更高精度，明智的做法是在成形之前先做出零件的放样图或展开图。可互换的结构件与非结构件，都是把平板料成形为槽形、角形、Z 形或帽形截面构件制成的。钣金件成形之前要先做展开图，以表明弯曲区需要多少材料、板料应在何处送入成形工具，以及折弯线位于何处。必须确定折弯线才能绘制钣金成形的展开图。

成形直的角弯时，必须为退让量和弯曲余量留出正确的余量。若采用收边或放边工艺，也必须留出余量，以便以最少的成形工作量做出零件。

### 制作直线弯

成形直线弯时，必须考虑材料的厚度、合金成分和回火状态。一般来说，材料越薄，能弯得越急（弯曲半径越小）；材料越软，弯得越尖。制作直线弯时还必须考虑的其他因素有弯曲余量、退让量以及折弯机线（对准线）。

板料的弯曲半径，是沿弯曲材料的内侧量得的弯曲半径。板料的最小弯曲半径，是板料在不使弯曲处金属严重削弱的前提下所能弯成的最急的弧或弯。弯曲半径过小，应力与应变会削弱金属，并可能导致开裂。

每种航空钣金都规定有最小弯曲半径。最小弯曲半径受材料种类、材料厚度和回火状态的影响。退火板料可弯到约等于其厚度的半径。不锈钢和 2024-T3 铝合金则需要相当大的弯曲半径。

#### 弯曲 U 形槽

为理解钣金放样的制作过程，下面讨论确定一个示例 U 形槽展开尺寸的各个步骤。使用弯曲余量计算时，求总展开长度的下列步骤既可用公式、图表，也可用计算机辅助设计（CAD）与计算机辅助制造（CAM）软件来完成。该槽由厚 0.040 英寸的 2024-T3 铝合金制成。

第 1 步：确定正确的弯曲半径　最小弯曲半径图表见制造厂维护手册。半径过急会使材料在弯曲过程中开裂。通常图纸会给出应使用的半径，但最好再复核一遍。对本放样示例，用图 4-124 的最小半径图表，按合金、回火状态和金属厚度选择正确的弯曲半径。对 0.040 英寸厚的 2024-T3，最小允许半径为 0.16 英寸（即 5/32 英寸）。

第 2 步：求退让量　退让量可用公式计算，也可在飞机维护手册或《来源、维护与可回收性》（SMR）手册中的退让量图表中查得。

用公式计算退让量　SB = 退让量，K = K 系数（90° 弯时 K 为 1），R = 弯曲内侧半径，T = 材料厚度。由于本示例中所有角都是 90°，退让量计算如下：SB = K(R+T) = 0.2 英寸。注：90° 弯时 K = 1。非 90° 弯时，使用“用退让量图表求退让量”所述的方法。退让量图表是快速求退让量的途径，对开口弯和闭合弯都适用，因为无需计算或查找 K 系数。有多种软件包和在线计算器可计算退让量，这些程序常与 CAD/CAM 程序配合使用。• 在图表底部以半径与材料厚度之和在相应刻度上取点；• 向上读到弯曲角；• 在左侧相应刻度上读出退让量。

示例：• 材料厚度为 0.063 英寸；• 弯曲角为 135°；• R + T = 0.183 英寸。

在图表底部找到 0.183，它位于中间刻度上。• 向上读到弯曲角 135°；• 在图表左侧中间刻度上定出退让量（0.435 英寸）。

第 3 步：求平直段长度尺寸　平直段长度尺寸可用公式求得：平直段 = MLD – SB，其中 MLD 为模线尺寸，SB 为退让量。U 形槽的平直段（平直部分）：两侧各等于模线尺寸减退让量，中间平直段等于模线长度减两个退让量。中间平直段要减两个退让量，是因为该平直段两侧各有一个弯。

示例 U 形槽的平直段尺寸按下述方法计算：

平直段尺寸 = MLD – SB；平直段 1 = 1.00 英寸 – 0.2 英寸 = 0.8 英寸；平直段 2 = 2.00 英寸 –（2 × 0.2 英寸）= 1.6 英寸；平直段 3 = 1.00 英寸 – 0.2 英寸 = 0.8 英寸。第 4 步：求弯曲余量　在金属上弯一个弯或折一道边时，必须算出弯曲余量，即该弯所需的材料长度。弯曲余量取决于四个因素：弯曲角度、弯曲半径、金属厚度和所用金属种类。

弯曲半径一般与材料厚度成正比。此外，弯曲半径越急，该弯所需的材料越少。材料种类也很重要：材料软，可以弯得很急；材料硬，弯曲半径就较大，弯曲余量也较大。弯曲角度影响金属的总长度，而厚度影响弯曲半径。

弯曲一块金属时，弧内侧的材料受压，弧外侧的材料受拉。然而，在这两个极端之间的某个距离上，存在一层不受这两种力影响的空间，称为中性线或中性轴，它位于距弯曲半径内侧约 0.445 倍金属厚度（0.445 × T）处。

必须确定这条中性轴的长度，以便为弯曲提供足够的材料，这个长度就是弯曲余量。该余量必须加到放样图的总长度上，以保证弯曲处有足够的材料。为节省计算弯曲余量的时间，人们已制定了针对各种角度、弯曲半径、材料厚度及其他因素的公式和图表。

公式 1：90° 弯的弯曲余量　在弯曲半径（R）上加金属厚度的一半（1/2 T），得 R + 1/2 T，即中性轴所在圆的半径。用中性线半径（R + 1/2 T）乘以 2π（注：π = 3.1416）求出该圆周长：2π(R + 1/2 T)。由于 90° 弯是圆周的四分之一，将周长除以 4，即得：

1/4 × 2π(R + 1/2 T)。这就是 90° 弯的弯曲余量。对半径为 1/4 英寸、材料厚 0.051 英寸的 90° 弯，代入公式如下：弯曲余量 = (2 × 3.1416)(0.250 + 1/2(0.051))/4 = 6.2832(0.250 + 0.0255)/4 = 6.2832(0.2755)/4 = 0.4327。弯曲余量（即该弯所需的材料长度）为 0.4327 英寸，即 7/16 英寸。

弯曲余量 = (0.01743R + 0.0078T)N，式中：

R = 所需弯曲半径，T = 金属厚度，N = 弯曲角度数。对半径 0.16 英寸、材料厚 0.040 英寸的 90° 弯使用本公式，代入如下：

弯曲余量 = (0.01743 × 0.16) + (0.0078 × 0.040) × 90 = 0.27 英寸。90° 弯弯曲余量图表的使用　图 4-128 中，弯曲半径示于顶行，金属厚度示于左列。每格中上面的数字是 90° 弯的弯曲余量，下面的数字是每 1° 弯曲的弯曲余量。求 90° 弯的弯曲余量，直接用图表中最上面的数字即可。

示例：U 形槽的材料厚度为 0.040 英寸，弯曲半径为 0.16 英寸。

沿弯曲余量图表顶行查找，找到弯曲半径 0.156 英寸所在的列；再在该列中找到与左列材料厚度（规格）0.040 相对应的一格。格中上面的数字为 0.273，即 90° 弯正确的弯曲余量（英寸）。

网上有若干弯曲余量计算程序，只需输入材料厚度、半径和弯曲角度，程序即可算出弯曲余量。

非 90° 弯的图表用法　若弯不是 90°，则用格中下面的数字（每 1° 的弯曲余量）来计算弯曲余量。

示例：图 4-129 所示的 L 形支架由 2024-T3 铝合金制成，自平板起的弯曲为 60°。注意图中标注的弯曲角为 120°，但那是两折边之间的角度，而不是自平板起的弯曲角。求正确弯曲角，用下式：

弯曲角 = 180° – 两折边间夹角。实际弯曲为 60°。求 0.040 英寸厚材料 60° 弯的正确弯曲半径，按下列步骤进行。

1. 在表左侧找到 0.040 英寸。

2. 向右找到弯曲半径 0.16 英寸（0.156 英寸）。

3. 记下格中下面的数字（0.003034）。

4. 用该数乘以弯曲角：0.003034 × 60 = 0.18204。第 5 步：求材料的总展开宽度　求出各平直段尺寸和弯曲余量后，即可计算总展开宽度（TDW）。计算 TDW 用下列公式：

TDW = 各平直段之和 +（弯曲余量 × 弯数）

对 U 形槽示例，得：

TDW = 平直段 1 + 平直段 2 + 平直段 3 +（2 × BA）

TDW = 0.8 + 1.6 + 0.8 +（2 × 0.27）

注意，制作该槽所需的金属量小于槽的外部尺寸（各模线尺寸之和为 4 英寸）。这是因为金属沿弯曲圆弧走，而不是沿模线逐段走。好的做法是核对算出的 TDW 小于各模线尺寸之和；若算出的 TDW 大于模线尺寸，则计算有误。

第 6 步：展开图放样　把全部有关信息在展开图上放样完毕后，即可将材料剪至正确尺寸，并在材料上画出折弯切线。

第 7 步：在展开图上画对准线　图 4-130 所放的样已基本完成，只差画一条对准线，以帮助把折弯切线正好定位在弯曲应开始的位置。在弯曲余量区内、距置于折弯机鼻梁下方的折弯切线一个弯曲半径处画一条线。把金属放入折弯机夹钳下，调整金属位置，使对准线正好在半径杆边缘的下方。然后夹紧折弯机，抬起折叶完成弯曲。弯曲正好从折弯切线处开始。

注：一个常见错误是把对准线画在弯曲余量区的正中，而不是画在距置于折弯机鼻梁下方的折弯切线一个半径处。

#### 用 J 图表计算总展开宽度

J 图表常见于 SRM 中，在已知弯曲内侧半径、弯曲角和材料厚度时，可用它确定弯曲扣除量（bend deduction）或退让量，以及展开图的总展开宽度。J 图表虽不如传统放样法精确，但对大多数应用而言能提供足够的信息。J 图表无需复杂的计算或背诵公式，因为所需信息可从修理图样中查到，或用简单的量具量出。

使用 J 图表时，最好先知道该角是开口角（大于 90°）还是闭合角（小于 90°），因为 J 图表的下半部用于开口角，上半部用于闭合角。

用 J 图表求总展开宽度的方法：

• 将直尺横放在图表上，把顶部刻度上的弯曲半径与底部刻度上的材料厚度连成一线。

• 在右侧刻度上找到该角度，沿该线水平向左，直至与直尺相交；• 在斜向弯曲的线上读出 X 系数（弯曲扣除量）；• 若 X 系数落在两线之间，则进行插值；• 把各模线尺寸相加，减去 X 系数，即得 TDW。

例 1　弯曲半径 = 0.22 英寸，材料厚度 = 0.063 英寸，弯曲角 = 90°，ML 1 = 2.00 / ML 2 = 2.00。用直尺把图表顶部的弯曲半径（0.22 英寸）与底部的材料厚度（0.063 英寸）连成一线，在右侧刻度上找到 90° 角，沿该线水平向左直至与直尺相交，再沿弯曲的线向左，在左侧读出 0.17，即图样中的 X 系数为 0.17 英寸。

总展开宽度 =（模线 1 + 模线 2）– X 系数；总展开宽度 =（2 + 2）– 0.17 = 3.83 英寸。例 2　弯曲半径 = 0.25 英寸，材料厚度 = 0.050 英寸，弯曲角 = 45°，ML 1 = 2.00 / ML 2 = 2.00。图 4-134 标出的是 135° 角，但那是两长边之间的夹角，自平板位置起算的实际弯曲为 45°（180 – 135 = 45）。用直尺把图表顶部的弯曲半径（0.25 英寸）与底部的材料厚度（0.050 英寸）连成一线，在右侧刻度上找到 45° 角，沿该线水平向左直至与直尺相交，再沿弯曲的线向左，在左侧读出 0.035，即图样中的 X 系数为 0.035 英寸。

总展开宽度 =（模线 1 + 模线 2）– X 系数；总展开宽度 =（2 + 2）– 0.035 = 3.965 英寸。盒式与盘式折弯机和檐口折弯机的调整方法相同。正确调整钣金折弯机是必需的，因为钣金弯曲的准确性取决于待成形材料的厚度与回火状态以及零件所需的半径。每当需要成形不同厚度的钣金，或零件需要不同半径时，操作者都必须在用折弯机成形零件之前对折弯机进行调整。本示例中要弯曲的是一条由 0.032 英寸厚 2024-T3 铝合金制成的 L 形槽。

### 用钣金折弯机折弯金属

#### 第 1 步：调整弯曲半径

弯曲零件所需的半径可从零件图样中查到；若图样未注明，则查阅 SRM 中的最小弯曲半径图表。该图表列出常用金属每种厚度和回火状态下允许的最小半径。弯曲比该半径更急会危及零件的完整性。弯曲区残留的应力可能使零件在使用中失效，即使弯曲时并未开裂。

钣金折弯机的半径杆可以换成另一种直径的半径杆。例如，0.032 英寸厚的 2024-T3 L 形槽需要弯成 1/8 英寸半径，就必须装上半径 1/8 英寸的半径杆。如果没有其他半径杆，而所装半径杆又小于零件所需，则必须弯制一些鼻梁半径垫片（nose radius shims）。

若半径小到使退火铝有开裂倾向，低碳钢是很好的垫片材料。必须用一小块边角料做试验，以确定使半径精确增大到 1/16 英寸或 1/8 英寸所需的厚度。用半径规和圆角规检查这一尺寸。此后每加一层垫片，都在原有半径上加一层。

示例：若原鼻梁为 1/16 英寸，在其上包弯一块 0.063 英寸厚（1/16 英寸）的材料，新的外半径即为 1/8 英寸。若再加一层 0.063 英寸（1/16 英寸），半径就成 3/16 英寸。若用 0.032 英寸（1/32 英寸）的材料代替 0.063 英寸（1/16 英寸）材料包在 1/8 英寸半径上，则得到 5/32 英寸半径。

#### 第 2 步：调整夹紧压力

下一步是设定夹紧压力。把一块与待弯零件同厚的材料滑到折弯机半径杆下方，向操作者方向拉夹紧手柄试验压力。这是偏心式夹钳，调整正确时，拉至完全夹紧位置不会有弹跳或松软的感觉。操作者必须能用有力的拉动把该手柄拉过死点，并使其撞到限位挡块。有些折弯机需在两侧分别调整。

在床面与夹钳之间距两端各 3 英寸处及中央各放一条试验条，调整夹紧压力，直至夹紧到足以防止工件在弯曲时滑移。夹紧压力可用夹紧压力螺母调整。

#### 第 3 步：调整鼻梁间隙

转动上夹爪后方的大号鼻梁间隙调整旋钮，使鼻梁间隙达到正确对位。理想的设定是：把折叶抬到成品弯曲的角度时，折叶与鼻梁半径件之间正好有一层材料厚度。用一块与待弯零件同厚的材料作塞尺，有助于达到很高的精度。［图 4-140、4-141］鼻梁间隙必须精确，沿待弯零件的整个长度上都应如此。检查方法：在距折弯机两端各 3 英寸处，于床面与夹钳之间各夹一条试验条，弯 90°，取下试验条对叠，两者应吻合；若不吻合，把弯得较尖的那一端稍微调回一些。

### 折制盒形件

盒形件可用与前文 U 形槽相同的方法成形，但当钣金件有相交的弯曲半径时，必须去除材料，为折边所占的材料让出空间。做法是在内侧折弯切线的交点处钻孔或冲孔。这些孔称为让位孔（relief holes），直径约为弯曲半径的两倍，可在弯曲时释放金属中的应力，防止金属撕裂。让位孔还能形成整齐的角部，便于从这里修去多余材料。

让位孔越大越光滑，角部形成裂纹的可能性就越小。让位孔的半径一般由图样规定。折制盒形件使用盒式与盘式折弯机，也称指形折弯机（finger brake）。先弯盒子的两个对边，然后调整折弯机的指板，使抬起折叶弯另外两边时，已折起的边能沿指板之间的缝隙向上让开。

让位孔的尺寸随材料厚度而变。对于厚度不超过 0.064 英寸（含）的铝合金板料，其直径不应小于 1/8 英寸；对于厚度 0.072～0.128 英寸的板料，不应小于 3/160 英寸。确定让位孔直径最常用的方法是以弯曲半径作为该尺寸，前提是它不小于最小允许值（1/8 英寸）。

#### 让位孔位置

让位孔必须与内侧折弯切线的交点相接触。为容许弯曲时可能出现的误差，应使让位孔越过内侧折弯切线 1/32～1/16 英寸。好的做法是以这些线的交点作为孔心。弧内侧的线朝让位孔方向斜切，以适应内侧折边的拉伸。

让位孔的位置很重要。其位置应使孔的外缘与内侧折弯切线的交点相接触，这样可以避免任何材料干扰另一个弯的弯曲余量区。若这两个弯曲余量区彼此相交，弯曲时该角部就会积聚很大的压应力，可能导致零件在弯曲时开裂。

#### 放样方法

用传统放样步骤对基本零件放样，由此确定各平直段宽度和弯曲余量。让位孔的位置由内侧折弯切线的交点来确定。作这两条相交线的角平分线，并沿该线向外移动一个孔半径的距离，此处即为孔心。在该点钻孔，然后修去角部剩余材料。修切通常与圆弧相切、与边缘垂直，从而留下一个开口角。若角部必须闭合，或需要稍长一点的折边，则相应修切。若角部要焊接，两折边在角部必须相互贴合。折边长度应比零件成品长度短一个材料厚度，以使只有折边的内侧相接触。

### 开口弯与闭合弯

开口弯与闭合弯有独特的难点，比 90° 弯需要更多的计算。下面 45° 弯与 135° 弯的示例中，材料厚 0.050 英寸，弯曲半径为 3/16 英寸。

#### 开口端弯（小于 90°）

图 4-147 示出 45° 弯的示例。1. 在 K 图表中查 K 系数，45° 的 K 系数为 0.41421 英寸。2. 计算退让量：SB = K(R + T) = 0.41421 英寸 ×（0.1875 英寸 + 0.050 英寸）= 0.098 英寸。3. 计算 45° 的弯曲余量：在弯曲余量图表中查出每 1° 的弯曲余量，再乘以 45：0.003675 英寸 × 45 = 0.165 英寸。4. 计算平直段：平直段 = 模线尺寸 – SB；平直段 1 = 0.77 英寸 – 0.098 英寸 = 0.672 英寸；平直段 2 = 1.52 英寸 – 0.098 英寸 = 1.422 英寸。5. 计算 TDW：TDW = 各平直段之和 + 弯曲余量 = 0.672 英寸 + 1.422 英寸 + 0.165 英寸 = 2.259 英寸。

可以看到，折弯机基准线仍然位于距折弯切线一个半径处。

#### 闭合端弯（大于 90°）

图 4-148 示出 135° 弯的示例。1. 在 K 图表中查 K 系数，135° 的 K 系数为 2.4142 英寸。2. 计算 SB：SB = K(R + T) = 2.4142 英寸 ×（0.1875 英寸 + 0.050 英寸）= 0.57 英寸。3. 计算 135° 的弯曲余量：在弯曲余量图表中查出每 1° 的弯曲余量，再乘以 135：0.003675 英寸 × 135 = 0.496 英寸。4. 计算平直段。

平直段 = 模线尺寸 – SB；平直段 1 = 0.77 英寸 – 0.57 英寸 = 0.20 英寸；平直段 2 = 1.52 英寸 – 0.57 英寸 = 0.95 英寸；TDW = 各平直段之和 + 弯曲余量 = 0.20 英寸 + 0.95 英寸 + 0.496 英寸 = 1.65 英寸。从两个示例可以明显看出，闭合弯的 TDW 比开口端弯小，材料长度需作相应调整。

### 手工成形

一切手工成形都围绕金属的放边（拉伸）与收边（收缩）这两个过程。如前所述，拉伸是指把金属某一区域拉长或增大，收缩是指使某一区域缩小。可根据待成形零件的尺寸、形状和轮廓，采用若干种拉伸与收缩方法。

例如，若要把成形角材或挤压角材弯成弧形，可以拉伸一边或收缩另一边，以能使零件贴合为准。在锤击成形（bumping）中，材料在凸起处被拉伸，使其鼓胀；在压窝（joggling）中，材料在两窝之间被拉伸。减重孔边缘的材料常被拉伸，以在孔周形成斜面的加强凸脊。下面几段讨论其中一些技法。

#### 直线弯

直线弯通常用檐口折弯机和折边机（bar folder）制作。没有这类机器时，较短的段可用木制或金属弯曲垫块手工弯曲。

板料放样并剪至尺寸后，沿折弯线把它夹在两块夹在台虎钳上的木制成形垫块之间。木制垫块的一条边应按所需弯曲半径倒圆，还应略弯过 90°，以补偿回弹。

用橡胶锤、塑料锤或生皮锤轻轻敲击，把伸出弯曲垫块之外的金属弯到所需角度。从一端开始敲击，沿边缘来回进行，使弯曲逐渐而均匀。如此反复，直至伸出的金属贴着成形垫块弯到所需角度。为补偿回弹，应把材料多弯过实际弯曲角一点。若伸出成形垫块的金属较多，要用手压住伸出的板料，防止其弹跳。消除不平整的方法是将一块平直硬木块侧立靠在弯曲处，用木槌或锤子重击。若伸出弯曲垫块的金属较少，则用硬木块和锤子完成整个弯曲。

#### 成形角材与挤压角材

成形角材与挤压角材都可通过拉伸或收缩其任一折边来弯成弧线（而不是急弯）。通常更倾向于用拉伸一侧折边的方法弯弧，因为该过程只需一个 V 形块和一把木槌，容易完成。

用 V 形块拉伸法　在拉伸法中，把要拉伸的折边放在 V 形块的槽内（若要收缩该折边，则把折边横放在 V 形块上）。用圆头软面锤在 V 形槽正上方轻而均匀地敲击折边，同时逐渐把折边压入 V 形槽。

从折边的一端开始，把条料缓慢来回移动，使锤击点均匀分布在折边上，逐渐而均匀地弯出弧线。握紧条料，以免敲击时弹跳。敲击过重会使金属起皱，因此要不断把折边在 V 形块上移动，但始终只在 V 形槽正上方轻敲。

在纸上或胶合板上放出足尺的准确样板，并定期检查弧线的准确性。把角材与样板比对，可准确判断弧线的进展以及何处需要加大或减小弧度。最好先使弧线大致符合所需形状，再着手精修某一部分，因为精修或整平角材可能使角材其他部分变形。若角材条料某处弯得过度，可把角材在 V 形块上翻转，使底边朝上，用木槌轻敲以减小弧度。

尽量以最少的锤击量弯出弧线，因为过度锤击会使金属加工硬化。加工硬化表现为金属对弯曲不再有反应，或出现弹性。有经验的工人很容易识别。某些情况下，弯弧过程中可能需要对零件进行退火；若如此，务必在装到飞机上之前对零件重新进行热处理。

用 V 形块与收边块收缩的方法　用收缩法把挤压或成形角材条料弯成弧线，可采用前述的 V 形块法或收边块法。V 形块法更快、更容易且对金属影响更小，因而更理想，但用收边块法也能取得良好效果。

在 V 形块法中，把角材条料的一边平放在 V 形块上，另一边朝上伸出。按拉伸部分所述的步骤，从条料一端开始来回轻敲。敲击折边边缘时要略带角度，以防立起的折边向外弯。

要不时用样板检查弧线的准确性。若弯得较急，角材（成形角材的横截面）会略微闭合。为避免角材闭合，可用小 C 形夹把角材条料夹在一块硬木板上，使被锤击的折边朝上。C 形夹的钳口应缠上遮蔽胶带。若角材已经闭合，用木槌敲几下或借助一小块硬木把折边恢复至正确角度。若条料某处弯得过度，可在 V 形块上翻转角材，用合适的木槌敲击以减小弧度，方法如前面拉伸一段所述。得到正确弧线后，用软面锤对整个角材进行精敲整平。

若成形角材的弧线较急，或角材的折边较宽，一般采用收边块法。此法是对要形成弧内侧的那条折边进行压褶（crimp）。

压褶时，握住压褶钳，使钳口相距约 1/8 英寸。来回转动手腕，使钳子上钳口先在下钳口一侧、再在另一侧接触折边。通过把隆起部分压入折边、逐渐加大钳子的扭转动作来完成压褶。压褶不要做得太大，否则难以敲平。压褶大小取决于材料的厚度和软硬，通常约 1/4 英寸即可。沿所需弧线均匀布置若干压褶，每个压褶之间留出足够间距，以便收边块的钳口容易夹上。

压褶完成后，把压过褶的折边放进收边块，使每次只有一个压褶位于钳口之间。用软面锤轻敲把每个压褶敲平，从压褶的顶点（闭合端）开始，逐渐向折边边缘推进。成形过程中要定期用样板检查角材弧线，所有压褶敲平后再检查一次。若需要加大弧度，可增加压褶并重复该过程。新增的压褶应布置在原压褶之间，以免金属在某一点过度加工硬化。若某处弧度需稍加大或减小，则使用 V 形块。

得到所需弧线后，在型砧或木模上对角材条料进行精敲整平。

#### 带折边角材

下面两种带折边角材的成形过程比前述角材稍复杂，因为弯折较短（不是逐渐弯成弧形），需要在很小或很集中的区域内收缩或拉伸。若折边要朝向弯曲内侧，材料必须收缩；若朝向外侧，则必须拉伸。

#### 收缩成形

用收缩法成形带折边角材时，使用与图 4-151 类似的木制成形垫块，步骤如下：

1. 把金属剪至尺寸，并留出成形后的修边余量。确定 90° 弯的弯曲余量，并据此把成形垫块的边缘倒圆。

2. 按图 4-151 把材料夹在成形垫块中，把露出的折边贴着垫块弯折。弯好后轻敲垫块，这会在弯曲处产生定型过程。

3. 用软面收缩锤从靠近中部开始锤击，逐渐向两端把折边压下去。由于材料被挤占的空间变小，折边在弯曲处容易起皱。要把材料敲成若干小皱而不是一个大皱，再通过轻敲、逐渐压实每一处小皱把它敲平。使用小块硬木楔块有助于消除皱褶。

4. 折边贴平成形垫块后对其进行精敲整平，消除小的不平整。若成形垫块是硬木的，用金属精敲锤；若垫块是金属的，用软面锤。修去多余材料并锉平、抛光。

#### 拉伸成形

用拉伸法成形带折边角材时，使用与收缩法相同的成形垫块、木楔块和锤子，步骤如下：

1. 把材料剪至尺寸（留修边余量），确定 90° 弯的弯曲余量，并把垫块边缘倒圆至所需弯曲半径。

2. 把材料夹在成形垫块中。

3. 用软面拉伸锤从靠近两端开始锤击，平稳而缓慢地把折边压下去，以防开裂或撕裂。按前一工序所述对折边和角材进行精敲整平，必要时修整并磨平边缘。

#### 带折边的弧形零件

带折边的弧形零件通常手工成形，其一侧为凹折边（内缘），另一侧为凸折边（外缘）。凹折边靠拉伸成形，凸折边靠收缩成形。这类零件借助硬木或金属成形垫块成形。垫块成对制作，专为所成形区域的形状设计，制作与识别方式与直线弯角材所用垫块相同；不同之处在于它们是为特定零件专门制作、彼此精确贴合，并与成品的实际尺寸和轮廓一致。

成形垫块可装小对位销，以便对正垫块并把金属固定就位；也可用 C 形夹或台虎钳夹在一起，或用螺栓穿过垫块和金属连接，前提是这些孔不影响成品强度。垫块边缘倒圆以给零件正确的弯曲半径，并内切约 5° 以补偿金属回弹。若材料较硬或弯曲必须精确，这一内切尤为重要。

翼肋前缘（nose rib）是成形弧形折边的好例子，因为它同时包含拉伸与收缩（压褶）。它通常有一侧凹折边（内缘）和一侧凸折边（外缘）。注意下列各图中的各种成形方式。在普通前缘肋中只用了一条大凸折边；由于绕零件一周的距离很长，且成形时容易起皱，它相当难成形。该肋的折边和压筋（钣金上用于加强的凸起棱）部分提供了足够强度，使其成为好用的型式。图 4-156 中凹折边难以成形，但外折边被让位孔分成若干小段。图 4-157 中可见压褶按等间距布置，以吸收材料并形成弧形，同时给零件增加强度。

图 4-158 中，前缘肋通过压褶、压筋、开让位孔并在两端各铆一条成形角材而成形。压筋和成形角材为零件提供强度。成形弧形折边的基本步骤如下：[图 4-159 与 4-160]

1. 把材料剪至尺寸，留约 1/4 英寸修边余量，并钻对位销孔。

2. 去除所有毛刺（锯齿状边缘）。这能降低成形过程中材料边缘开裂的可能。

3. 确定并钻对位销孔。4. 把材料放在成形垫块之间，用台虎钳夹紧，防止材料移动或错位。夹持应尽可能靠近正在锤击的区域，以免成形垫块受力变形并使金属滑动。

凹面　先弯凹曲线上的折边。这样做可防止金属拉伸时折边裂开或开裂；一旦裂开，就必须重做新件。用面稍呈圆形的塑料锤或生皮锤，从零件最两端开始锤击，逐步向弯曲中部推进，使端部部分金属被赶向弧线中部需要材料之处。持续锤击，直至整个折边逐渐贴合成形垫块。折边成形后修去多余材料，并检查零件精度。

凸面　凸面靠在成形垫块上收缩材料成形。用木制或塑料收缩锤和垫块（或楔块），从弧线中部开始向两端推进。把折边沿模具锤下去，以约 45° 的斜击方式敲击金属，动作方向要倾向于把零件从垫块半径处拉开。在弯曲半径处拉伸金属，并在楔块上锤击逐渐消除皱褶。用垫块使折边边缘尽可能垂直于成形垫块，它还能减少起皱、撕裂或开裂的可能。最后修去折边多余金属、精敲整平、去毛刺、倒圆角（若有），并检查零件精度。

#### 锤击成形

如前所述，锤击成形（bumping）是把钣金敲入模具使其鼓胀而实现拉伸。锤击成形可在成形垫块或凹模上进行，也可在砂袋上进行。

两种方法都只需要一个模具：木块、铅模或砂袋。鼓包（blister，即流线型盖板）就是用成形垫块或模具锤击法制作的零件示例；机翼整流包皮则通常用砂袋锤击成形。

成形垫块或模具　用于垫块锤击成形的木块或铅模，其尺寸和轮廓必须与鼓包外侧相同。为提供足够的顶铁重量和固定金属的支承面，垫块或模具各方向尺寸应比所需成形尺寸至少大 1 英寸。制作成形垫块的步骤如下：1. 用锯、凿、圆凿、锉刀和粗锉等工具把木块掏空。

2. 用砂纸把木块打磨光滑。模具内表面必须尽可能光滑，因为任何微小不平都会反映到成品上。

3. 按图 4-161 制作若干样板（横截面样板），以便检查模具精度。

4. 在 1、2、3 点处修出模具轮廓。

5. 修整样板检查点之间的区域，使其余轮廓与 4 号样板一致。修整模具需格外小心，因为模具越精确，做出光滑成品所需时间越少。

模具制作并检查完毕后，按下列步骤进行锤击成形：

1. 把板料剪至尺寸，多留 1/2 至 1 英寸以便拉形。

2. 在模具和铝板上涂一薄层轻质油，以防擦伤（在粗糙处刮伤）。

3. 把材料夹在模具与钢板之间。确保其支承牢固，但仍能向模具内侧稍微滑移。

4. 把锤击垫块夹在台虎钳上。用软面橡胶锤，或用硬木传力块配适当锤子，从模具边缘附近开始锤击。

5. 用轻敲从边缘开始逐渐把材料压下去。记住，锤击成形的目的是靠拉伸把材料赶成形，而不是用重击把它硬压进模具。始终从模具边缘附近开始锤击，绝不要从鼓包中心开始。

6. 从模具上取下工件前，用枫木块或拉伸锤的圆头摩擦，尽量把表面压光。

7. 把鼓包从锤击垫块上取下，修剪至尺寸。

砂袋锤击成形　砂袋锤击成形是钣金手工成形中最难的方法之一，因为没有精确的成形垫块引导操作。此法是在砂袋上压出一个凹坑，以容纳金属被锤击部分的形状。凹坑会因锤击而移位，因此锤击过程中需定期重新修整。移位程度主要取决于所成形件的轮廓或形状，以及是否必须用斜击来拉伸、拉形或收缩金属。用此法成形时，要准备轮廓样板或某种靠模作为操作基准，以保证成品精度。样板可用普通牛皮纸或类似纸张制作，把它覆在要仿制的零件上折叠。在需要拉伸才能贴合处剪开纸罩，并用遮蔽胶带粘上附加纸片盖住露出的部分。完全覆盖零件后，把样板修剪至准确尺寸。

展开样板，把它摊在将要成形该零件的金属上。样板虽不能平铺，但能相当准确地示出所需切割金属的大致形状，拼补的片段则指示何处需要拉伸。样板放到材料上后，用毡头笔描出零件及需拉伸部分的轮廓。剪料时至少多留 1 英寸余量，零件锤击成形后再修去多余金属。

若要成形的零件是径向对称的，则相当容易成形，因为可用简单的轮廓样板作为操作基准。在砂袋上锤击钣金件遵循若干基本步骤，不论零件轮廓或形状如何都可适用。

1. 放出并剪出轮廓样板，作为操作基准并保证成品精度。（样板可用钣金、中厚纸板、牛皮纸或薄胶合板制作。）

2. 确定所需金属量，放出并剪至尺寸，至少多留 1/2 英寸。

3. 把砂袋放在能承受重击的坚实基础上，用光面锤在袋上压出一个凹坑。分析零件，确定凹坑在成形时应有的正确半径。凹坑会随锤击而变形，须相应重新修整。

4. 选一把软面圆头或钟形锤，其轮廓略小于钣金件所需轮廓。左手握住金属一边，把要锤击的部位放在砂袋凹坑边缘附近，用轻斜击敲打金属。

5. 继续向中心锤击，转动金属，逐渐向内推进，直至得到所需形状。要把整个零件作为一个整体来成形。

6. 锤击过程中常用样板检查零件形状精度。若出现皱褶，要在其变大之前消除。

7. 用合适的型砧和精敲锤，或用平锤（hand dolly）和精敲锤，消除小凹痕和锤印。

8. 锤击完成后，最后用圆规（dividers）沿物件外侧划线。修剪边缘并锉光。清洁并抛光零件。

#### 压窝

压窝（joggle）常见于长桁与隔框的交接处，是在零件上做出的偏置，为板材或另一配合件让出间隙。采用压窝可保持接头或对接处的表面平整。偏置量通常很小，因此压窝深度一般以千分之一英寸给出。压窝深度由需要让开的材料厚度决定。确定压窝所需长度时，要额外留 1/16 英寸，以增加足够间隙，保证压窝后的搭接件能贴合。压窝两弯之间的距离称为压窝余量（allowance）。该尺寸通常在图样上标注；但估算余量的经验法则是平板位移量的四倍厚度。对 90° 角，由于压窝时弯曲半径处产生的应力，余量须稍大。对挤压件，余量可达材料厚度的 12 倍，因此务必按图样施工。

压窝的成形方法有多种。例如，若压窝要作在直折边或平板上，可在檐口折弯机上成形。成形压窝的步骤如下：

1. 在板上放出压窝各弯折处的边界线。

2. 把板料插入折弯机，把金属弯起约 20°~30°。

3. 松开折弯机，取出零件。

4. 翻转零件，在第二条弯折线处夹入折弯机。

5. 把零件弯起，直至达到正确的压窝高度。

6. 从折弯机上取下零件，检查压窝尺寸与间隙是否正确。

若压窝需作在弧形零件或弧形折边上，可用硬木、钢或铝合金制成的成形垫块或模具。成形时把要压窝的零件放在两块压窝模之间，在台虎钳或其他合适夹紧装置中压紧。压窝成形后，把压窝模在台虎钳中翻转，用木槌或生皮槌把另一折边上的凸起敲平。

由于硬木易于加工，模具只用几次时用硬木制作即可满足要求。若需制作大量同类压窝，则应使用钢模或铝合金模。铝合金模更受青睐，因为它比钢模更容易制造，寿命也大致相当。这类模具足够软而有弹性，可在其上成形铝合金零件而不致划伤，且表面的磕痕和划痕容易去除。

首次使用压窝模时，要先在废料上试模以检查精度，避免损坏已加工好的零件。始终保持模块表面无污物、锉屑等，以免划伤工件。

#### 减重孔

在翼肋段、机身隔框和其他结构件上开减重孔以减轻重量。为避免因去除材料而削弱构件，常在孔周压出折边，以加强被去掉材料的区域。

未经批准，绝不得在任何结构件上开减重孔。减重孔的尺寸和孔周折边的宽度由设计规范确定。规范中已考虑安全裕度，使零件在减重的同时仍保留必要强度。减重孔可用孔锯、冲头或飞刀（fly cutter）加工。边缘要锉光，以防开裂或撕裂。

减重孔翻边　用翻边模或硬木、金属成形垫块压出折边。翻边模由两个配合件组成：凹模与凸模。翻软金属时，模具可用枫木等硬木；翻硬金属或需长期使用时，应使用钢模。导销应与待翻边的孔同尺寸，台肩的宽度与角度应与所需折边一致。

翻减重孔折边时，把材料放在模具的配合件之间，通过锤击或在台虎钳、手扳压床（arbor press，一种小型手动压床）中压合模具成形。模具涂一层轻质机油后工作更顺畅。

### 不锈钢的加工

当需要高强度时，飞机某些零件使用耐蚀钢（CRES）板。CRES 与镁、铝或镉接触时会使这些金属腐蚀。为把 CRES 与镁、铝隔离，要在其配合面之间施加防护涂层。弯曲半径应大于推荐的最小弯曲半径，以防弯曲区材料开裂，这一点很重要。

加工不锈钢时，务必不使金属受到过度划伤或损伤。剪切、冲孔或钻孔时也要特别小心。剪或冲不锈钢所需压力约为低碳钢的两倍。剪床或冲模的间隙要调得很小。间隙过大会使金属被拉过模刃，造成加工硬化，从而使机器承受过大应力。钻不锈钢时，使用顶角磨成 135° 的高速钢钻头。钻速约为钻低碳钢的一半，但绝不要超过 750 r/min。对钻头施加均匀压力，使进给始终恒定。要在铸铁等衬板上钻孔，衬板硬度足以让钻头完全钻穿而不会把金属推离钻尖。通电前先定心（spot），并确保通电时已施加压力。

### Inconel® 625 与 718 合金

Inconel® 指一类镍铬铁高温合金，典型用于高温场合。耐腐蚀性和高温下保持强度的能力，使这些 Inconel® 合金常用于飞机动力装置结构。Inconel® 625 和 718 合金可按钢和不锈钢的常规工艺冷成形。

在 Inconel® 合金上常规钻孔时，钻头容易折断，且钻头穿透金属时会损伤孔边。若用手电钻钻 Inconel® 625 和 718 合金，应选 135° 钴钻头。手钻时要用力压钻，但保持恒定切屑率。例如钻 30 号孔时，约用 50 磅力推压钻头。按图 4-166 所示使用最大钻速。手钻时不必使用切削液。

推荐的钻孔程序如下：

• 用动力进给设备在松散的修理件上钻出导孔，然后再预装配。

• 预装配修理件，并在配合结构上钻导孔。

• 把导孔扩至最终孔径。

钻 Inconel® 时，最好使用自动进给式钻孔设备。

### 镁的加工

警告：让镁屑远离火源。镁的小颗粒极易燃烧。浓度足够时，这些小颗粒会引起爆炸。水接触熔融镁可能引发蒸汽爆炸。镁火用干滑石粉、碳酸钙、砂或石墨扑灭，把粉末覆盖在燃烧的金属上，厚度 1/2 英寸以上。不得使用泡沫、水、四氯化碳或二氧化碳。镁合金不得接触甲醇。

镁是世界上最轻的结构金属。与许多其他金属一样，这种银白色元素不以纯态用于承力场合；而是与其他金属（铝、锌、锆、锰、钍和稀土金属）制成合金，以获得结构用所需的高强度轻质合金。与其他金属合金化后，镁可得到性能优良、比强度高的合金。合理配比这些合金元素，可得到适于砂型铸造、金属型铸造和压铸、锻造、挤压、轧制板材和厚板，且在室温和高温下性能均良好的合金。

轻质是镁最著名的特性，也是飞机设计中的一个重要因素。相比而言，铝的重量是其 1.5 倍，钢铁是其 4 倍，铜和镍合金是其 5 倍。镁合金可用与钢或黄铜相同的工具切割、钻孔和铰孔，但刀刃必须锋利。铆接镁合金零件时使用 B 型铆钉（5056-F 铝合金）。镁零件常用包铝 2024-T3 铝合金修理。

镁合金通常可用与其他金属类似的方法加工，但要注意许多车间工艺细节不能照搬。镁合金在室温下难以加工，因此大多数工序必须在高温下进行，这需要预热金属或模具，或两者都预热。镁合金板可用刀刃剪、落料模、铣刀或锯切割。挤压件通常用手锯或圆锯切至长度。绝不要用普通剪床和冲剪机切割镁合金板，因为它们会产生粗糙、开裂的边缘。

镁合金的剪切和落料要求严格的模具公差，建议最大间隙为板厚的 3%~5%。剪床上刀刃应磨成 45°~60° 的顶角。冲头的剪切角应为 2°~3°，凹模间隙角 1°。落料时，凹模剪切角为 2°~3°，冲头间隙角 1°。应尽可能使用压料装置。硬轧板厚超过 0.064 英寸、退火板厚超过 1/8 英寸时不得冷剪。经过剪切的镁板边缘粗糙起鳞，可用修切（shaving）整平，即第二次剪切去除约 1/32 英寸。

有时采用热剪以获得更好的剪切边缘，这对厚板和厚料是必要的。退火板可加热至 600 °F，但硬轧板必须保持在 400 °F 以下，具体取决于所用合金。热膨胀要求考虑冷却后的收缩，即在加工前把冷态金属尺寸加大一点。

厚度超过 1/2 英寸的厚板只能用锯切。切厚板或厚重挤压件时，推荐使用 4~6 齿/英寸的粗齿（raker-set）带锯条。小型和中型挤压件用每英寸 6 齿的圆锯机更易切割。板料可用 8 齿/英寸的粗齿或直齿手锯切割。带锯应装无火花导锯块，以消除火花引燃镁合金锉屑的危险。

大多数镁合金在室温下的冷加工非常有限，因为它们会迅速加工硬化，不适合任何剧烈的冷成形。板材可进行一些简单弯曲，但软材料弯曲半径至少为板厚的 7 倍，硬材料至少为板厚的 12 倍。若在成形前加热材料，可用板厚 2~3 倍的半径。

由于变形镁合金冷加工后容易开裂，最好在尝试任何成形工序前把金属加热到 450 °F。在较低温度范围内成形的零件强度更高，因为较高温度会对金属产生退火作用。

热加工镁的缺点是：

1. 加热模具和材料费用高且麻烦。

2. 在这些温度下润滑和搬运材料存在问题。

热加工镁的优点是：

1. 热态下比其他金属更容易成形。

2. 回弹减小，尺寸精度更高。

加热镁及其合金时要密切注意温度，因为金属容易烧损。过热还会在金属内部形成小的熔池。无论哪种情况，金属都会报废。为防止燃烧，加热镁时必须用二氧化硫气氛保护。

绕小半径正确弯曲时，需去除弯曲线附近的尖角和毛刺。放样应用木工软铅笔，因为表面任何划伤都可能导致疲劳裂纹。

压弯机可用于制作小半径弯曲。需作直角弯曲时，应采用模具和橡胶法，因为直角弯使折弯机的使用变得复杂。滚弯可在为铝材设计的设备上冷作。镁最常见的成形和浅拉形方法是用橡胶垫作凹模：橡胶垫装在一个倒置的钢盆中，由液压机滑块下压。压机对金属施加压力，使其贴合凸模形状。

镁合金的切削加工性极好，可在机床上采用最高速度、大切深和高进给。加工镁合金的功率需求约为低碳钢的六分之一。

切削产生的锉屑、切屑和碎屑应存放在有盖的金属容器中，因为存在燃烧危险。不得在液体除冰和喷水系统中，或整体油箱区域使用镁合金。

### 钛的加工

让钛屑远离火源。钛的小颗粒极易燃烧。浓度足够时会引起爆炸。水接触熔融钛可能引发蒸汽爆炸。钛火用干滑石粉、碳酸钙、砂或石墨扑灭，把粉末覆盖在燃烧的金属上，厚度 1/2 英寸以上。不得使用泡沫、水、四氯化碳或二氧化碳。

#### 钛的概述

钛在矿物状态下是地壳中储量第四丰富的结构金属。它质轻、无磁、强度高、耐蚀且延展性好。钛的模量、密度和中等温度下的强度介于铝合金与不锈钢之间。钛比钢强 30%，但轻近 50%；比铝重 60%，但强度是铝的两倍。

钛及其合金主要用于要求良好耐蚀性、600 °F（315 °C）以下中等强度和轻质的零件。工业纯钛板可用液压成形机、拉形机、滚弯成形、落锤或其他类似工序成形。它比退火不锈钢更难成形。钛也可用磨、钻、锯以及其他金属所用的加工方式加工。钛必须与镁、铝或合金钢隔离，因为接触时其他金属会发生电偶腐蚀或氧化。

安装钛零件时应使用 Monel® 铆钉或标准紧公差钢紧固件。合金板可在室温下有限度地成形。钛合金的成形分为三类：

• 无应力消除的冷成形 • 有应力消除的冷成形 • 高温成形（自带应力消除）

美国生产的钛中，超过 5% 是以 Ti-6Al-4V 合金形式生产的，该合金被称为钛工业的“主力军”。Ti-6Al-4V 用于飞机涡轮发动机部件和飞机结构件，强度约为纯钛的 3 倍。作为应用最广的钛合金，它难以成形。

以下是 Ti-6Al-4V 退火态带应力消除的冷成形（室温成形）程序：

1. 成形钛时使用最小半径图表很重要，因为半径过小会给弯曲区引入过大应力。

2. 对零件进行应力消除：把零件加热到 1,250 °F（677 °C）以上、1,450 °F（788 °C）以下，在此温度保持 30 分钟以上、10 小时以下。

3. 成形钛零件需要大功率压弯机。普通手动盒盘折弯机（box and pan brake）无法成形钛板。

4. 若修理补片需要弯曲以贴合飞机外形，常使用电动滚板机（power slip roller）。

钛可能难以钻孔，但只要钻头锋利、施加足够压力并使用低速钻机，仍可使用标准高速钢钻头。若钻头磨钝，或任其在半钻孔中空转，会产生过热状态，使后续钻孔极其困难。因此，孔应尽量浅；使用经批准设计的短而锋利的钻头；并大量浇注切削液，以便钻孔或铰孔。

加工钛时，建议使用硬质合金或含钴 8% 的钻头、铰刀和锪钻。从孔中取出钻头或铰刀时，要让其保持旋转，以免划伤孔壁。只有在没有强制进给钻机时才使用手电钻。

钻钛时遵循以下准则：

• 一次钻出的最大孔径为 0.1563 英寸，因为需要很大的力。

直径更大的钻头在施加很大力时切削效果不佳。切削效果不佳的钻头会损伤孔。

• 直径 0.1875 英寸及以上的孔，若操作者符合下列条件，可用手电钻：

- 从直径 0.1563 英寸的孔开始。

- 以 0.0313 或 0.0625 英寸的增量扩大孔径。

• 钴钒钻头比高速钢钻头耐用得多。

• 手钻钛的推荐钻机转速列于图 4-167。

• 钻钛时钻头寿命比钻钢短。不要使用钝钻头，也不要让钻头在金属表面摩擦而不切削。若出现上述情况，钛表面会加工硬化，再想重新起钻就非常困难。

• 同时手钻两个或多个钛零件时，要把它们紧紧夹在一起。可用临时螺栓、Cleco 夹或工装夹夹紧。夹子要布置在待钻区域周围，并尽量靠近该区域。

• 手钻薄件或柔性件时，在零件背面加支撑（如木块）。

• 钛的导热性低。变热后，其他金属容易与其粘连。钻速过高时，钛颗粒常会焊在钻头的锋利刃口上。钻大板或挤压件时，使用水溶性冷却液或硫化油。

注：金属加工过程中金属与金属的紧密接触会产生热量和摩擦，必须加以减少，否则所用工具和钣金会很快损坏和/或报废。冷却剂（也称切削液）通过把热量从工具和钣金带走，减少工具与钣金界面处的摩擦。因此，使用切削液可提高生产率、延长工具寿命，并带来更高的加工质量。

## 3. 专业词汇

| 英文 | 词性 | 中文 | 本节语境 |
| --- | --- | --- | --- |
| layout | n./v. | 放样；划线 | 按图样在板料上划出弯曲线、孔位与轮廓的过程 |
| flat pattern | n. | 展开图；展开料 | 把成形件摊平后得到的平面形状与下料尺寸 |
| bend allowance | n. | 弯曲余量 | 两条折弯切线之间那段圆弧的材料长度 |
| setback (SB) | n. | 退让量 | 折弯机钳口相对模线后退的距离，90° 弯时 SB=R+T |
| bend tangent line | n. | 折弯切线 | 金属开始弯曲和停止弯曲的位置线 |
| K-factor | n. | K 系数 | 非 90° 弯计算退让量时用的系数，随弯曲角度变化 |
| sight line | n. | 视线；折弯基准线 | 与折弯机鼻端对齐的划线，弯曲时作对准基准 |
| mold line (ML) | n. | 模线 | 零件平直侧面越过圆弧的延长线 |
| total developed width (TDW) | n. | 总展开宽度 | 沿弯曲量到边的材料总宽，用来确定下料尺寸 |
| neutral axis | n. | 中性轴 | 弯曲前后长度保持不变的假想线 |
| flange | n. | 折边；凸缘 | 弯边形成的窄条，也指孔周压出的加强边 |
| joggle | n./v. | 压窝；偏置 | 长桁与隔框交接处为让开板材做出的台阶形偏置 |
| relief hole | n. | 让位孔 | 开在折弯切线交点处、防止弯曲撕裂的小孔 |
| shrinking | n. | 收边；收缩 | 用压褶使金属某区域面积减小的成形方法 |
| stretching | n. | 放边；拉伸 | 用锤击把金属某区域拉长、展宽的成形方法 |
| bumping | n. | 锤击成形 | 把板料敲入模具或砂袋凹坑使其鼓胀成形的工艺 |

## 4. 语法解析

### ① 破折号引出同位语，后接定语从句定义术语
**原句**：Bend tangent line (BL)—the location at which the metal starts to bend and the line at which the metal stops curving.
**拆解**：主语是术语 `Bend tangent line (BL)`，破折号后 `the location ... and the line ...` 是两个并列名词短语作同位语，各自带 `at which` 引导的定语从句，说明"开始弯"与"停止弯"两个位置。
**要点**：技术手册定义术语惯用"术语—名词短语+定语从句"的写法；`at which` 在此等于 `where`，指代前面的 location/line，翻译时把定语从句前置成"……的位置线"更合中文语序。

### ② 定语从句 + as ... as 比较状语从句
**原句**：Neutral axis—an imaginary line that has the same length after bending as it had before bending.
**拆解**：`that has the same length ... as it had ...` 中 `that` 引导定语从句修饰 `line`，从句内 `the same ... as ...` 构成比较，`as it had` 后省略了 `before bending` 已出现的 `length`；`after bending` 与 `before bending` 形成时间对照。
**要点**：`the same + 名词 + as` 是固定比较结构，不可写成 `the same ... like`；英文靠省略避免重复，中文须补出"长度"才通顺。

### ③ 动名词短语作主语
**原句**：Finding the TDW is necessary to determine the size of material to be cut.
**拆解**：`Finding the TDW` 是动名词短语作主语，谓语用单数 `is`；`to determine ...` 作目的状语，其中 `to be cut` 是不定式被动式，后置修饰 `material`。
**要点**：`the size of material to be cut` 这类"名词 + of + 名词 + to be done"结构在工艺文件中极常见，译作"待切割材料的尺寸"，被动不定式表"将要被……"。

### ④ 情态动词被动语态 + 定语从句限定范围
**原句**：The K-factor must be used for all bends that are smaller or larger than 90°.
**拆解**：`must be used` 为情态动词 + 被动语态，突出"必须采用"的规程语气；`that are smaller or larger than 90°` 修饰 `bends`，把 90° 以外的弯全部纳入。
**要点**：规范类文本用 `must be + 过去分词` 表达强制要求；`smaller or larger than` 用一对反义比较词把区间"非 90°"说全，比 `not equal to` 更具体。

### ⑤ 不定式被动式作后置定语，主谓看中心词
**原句**：The thickness of the material to be cleared governs the depth of the joggle.
**拆解**：主语中心词是 `The thickness`，`of the material` 与 `to be cleared` 依次后置限定；谓语 `governs` 用单数，与 `thickness` 一致而非与 `material` 一致。
**要点**：`of + 名词 + to be + 过去分词` 是"待处理对象"的紧凑写法；翻译时先抓到中心词 thickness，避免被中间名词带偏主谓。

### ⑥ 介词短语前置 + while 分词短语表伴随
**原句**：For 90° angles, it must be slightly more due to the stress built up at the radius while joggling.
**拆解**：`For 90° angles` 前置状语点明适用范围；主句 `it must be slightly more` 中 `it` 指前文的 allowance；`due to the stress built up ...` 说明原因，`built up at the radius` 是过去分词短语后置修饰 `stress`，`while joggling` 为省略主语的时间/伴随状语。
**要点**：`due to + 名词` 在技术文中表原因，比从句简洁；`stress built up`＝"积聚起来的应力"，过去分词短语作定语要译成主动的"……的"。
