# Radio Navigation

> 机体 Ch 11 · Radio Navigation · 原文 PDF 第 643 页

## 1. 原文

In the early years of aviation, a compass, a map, and dead reckoning were the only navigational tools. These were marginally reassuring if weather prevented the pilot from seeing the terrain below. Voice radio transmission from someone on the ground to the pilot indicating that the aircraft could be heard overhead was a preview of what electronic navigational aids could provide. For aviation to reach fruition as a safe, reliable, consistent means of transportation, some sort of navigation system needed to be developed.

Early flight instruments contributed greatly to flying when the ground was obscured by clouds. Navigation aids were needed to indicate where an aircraft was over the earth as it progressed toward its destination. In the 1930s and 1940s, a radio navigation system was used that was a low frequency, four-course radio range system. Airports and selected navigation waypoints broadcast two Morse code signals with finite ranges and patterns. Pilots tuned to the frequency of the broadcasts and flew in an orientation pattern until both signals were received with increasing strength. The signals were received as a blended tone of the highest volume when the aircraft was directly over the broadcast area. From this beginning, numerous refinements to radio navigational aids developed.

Radio navigation aids supply the pilot with intelligence that maintains or enhances the safety of flight. As with communication radios, navigational aids are avionics devices, the repair of which must be carried out by trained technicians at certified repair stations. However, installation, maintenance and proper functioning of the electronic units, as well as their antennas, displays, and any other peripheral devices, are the responsibilities of the airframe technician.

### VOR Navigation System

One of the oldest and most useful navigational aids is the very high frequency omni-directional range (VOR) navigation system. The four main components of a typical system are: a receiver, a visual indicator, a frequency selector (controller or control panel), and antennas. The system was constructed after WWII and is still in use today. It consists of thousands of land-based transmitter stations, or VORs, that communicate with radio receiving equipment on board aircraft. Many of the VORs are located along airways. The Victor airway system is built around the VOR navigation system. Ground VOR transmitter units are also located at airports where they are known as TVOR (terminal VOR). The U.S. Military has a navigational system known as TACAN that operates similarly to the VOR system. Sometimes VOR and TACAN transmitters share a location. These sites are known as VORTACs.

The position of all VORs, TVORs, and VORTACs are marked on aeronautical charts along with the name of the station, the frequency to which an airborne receiver must be tuned to use the station, and a Morse code designation for the station. Some VORs also broadcast a voice identifier on a separate frequency that is included on the chart.

VOR uses VHF radio waves (108–117.95 MHz) with 50 kHz separation between each channel. This keeps atmospheric interference to a minimum but limits the VOR to line-of- sight usage. To receive VOR VHF radio waves, generally a V-shaped, horizontally polarized, bi-pole antenna is used. Other type antennas are also certified. Follow the manufacturer’s instructions for installation location.

The signals produced by a VOR transmitter propagate 360° from the unit and are used by aircraft to navigate to and from the station with the help of an onboard VOR receiver and display instruments. A pilot is not required to fly a pattern to intersect the signal from a VOR station since it propagates out in every direction. The radio waves are received as long as the aircraft is in range of the ground unit and regardless of the aircraft’s direction of travel.

A VOR transmitter produces two signals that a receiver on board an aircraft uses to locate itself in relation to the ground station. One signal is a reference signal. The second is produced by electronically rotating a variable signal. The variable signal is in phase with the reference signal when at magnetic north but becomes increasingly out of phase as it is rotated to 180°. As it continues to rotate to 360° (0°), the signals become increasingly in phase until they are in phase again at magnetic north. The receiver in the aircraft deciphers the phase difference and determines the aircraft’s position in degrees from the VOR ground based unit.

Most aircraft carry a dual VOR receiver. Sometimes, the VOR receivers are part of the same avionics unit as the VHF communication transceiver(s). These are known as NA V/ COM radios. Internal components are shared since frequency bands for each are adjacent.

Large aircraft may have two dual receivers and even dual antennas. Normally, one receiver is selected for use and the second is tuned to the frequency of the next VOR station to be encountered en route. A means for switching between NA V 1 and NA V 2 is provided as is a switch for selecting the active or standby frequency. VOR receivers are also found coupled with instrument landing system (ILS) receivers and glideslope receivers.

AVOR receiver interprets the bearing in degrees to (or from) the VOR station where the signals are generated. It also produces DC voltage to drive the display of the deviation from the desired course centerline to (or from) the selected station. Additionally, the receiver decides whether or not the aircraft is flying toward the VOR or away from it. These items can be displayed a number of different ways on various instruments. Older aircraft are often equipped with a VOR gauge dedicated to display only VOR information. This is also called an omni-bearing selector (OBS) or a course deviation indicator (CDI). relation to the VOR station regardless of the aircraft’s direction of The CDI linear indicator remains essentially vertical but moves left and right across the graduations on the instrument face to show deviation from being on course. Each graduation represents 2°. The OBS knob rotates the azimuth ring. When in range of a VOR, the pilot rotates the OBS until the course deviation indicator centers. For each location of an aircraft, the OBS can be rotated to two positions where the CDI will center. One produces an arrow in the TO window of the gauge indicating that the aircraft is traveling toward the VOR station. The other selectable bearing is 180° from this. When chosen, the arrow is displayed in the FROM window indicating the aircraft is moving away from the VOR on the course selected. The pilot must steer the aircraft to the heading with the CDI centered to fly directly to or from the VOR. The displayed VOR information is derived from deciphering the phase relationship between the two simultaneously transmitted signals from the VOR ground station. When power is lost or the VOR signal is weak or interrupted, a NA V warning flag comes into view.

A separate gauge for the VOR information is not always used. As flight instruments and displays have evolved, VOR navigation information has been integrated into other instruments displays, such as the radio magnetic indicator (RMI), the HSI, an EFIS display or an electronic attitude director indicator (EADI). Flight management systems and automatic flight control systems are also made to integrate VOR information to automatically control the aircraft on its planned flight segments. Flat panel MFDs integrate VOR information into moving map presentations and other selected displays. The basic information of the radial bearing in degrees, course deviation indication, and to/from information remains unchanged however.

At large airports, an instrument landing system (ILS) guides the aircraft to the runway while on an instrument landing approach. The aircraft’s VOR receiver is used to interpret the radio signals. It produces a more sensitive course deviation indication on the same instrument display as the VOR CDI display. This part of the ILS is known as the localizer and is discussed below. While tuned to the ILS localizer frequency, the VOR circuitry of the VOR/ILS receiver is inactive. It is common at VOR stations to combine the VOR transmitter with distance measuring equipment (DME) or a nondirectional beacon (NDB) such as an ADF transmitter and antenna. When used with a DME, pilots can gain an exact fix on their location using the VOR and DME together. Since the VOR indicates the aircraft’s bearing to the VOR transmitter and a co-located DME indicates how far away the station is, this relieves the pilot from having to fly over the station to know with certainty their location. These navigational aids are discussed separately in the following sections.

Functional accuracy of VOR equipment is critical to the safety of flight. VOR receivers are operationally tested using VOR test facilities (VOT). These are located at numerous airports that can be identified in the Airport Facilities Directory for the area concerned. Specific points on the airport surface are given to perform the test. Most VOTs require tuning 108.0 MHz on the VOR receiver and centering the CDI. The OBS should indicate 0° showing FROM on the indicator or 180° when showing TO. If an RMI is used as the indicator, the test heading should always indicate 180°. Some repair stations can also generate signals to test VOR receivers although not on 108.0 MHz. Contact the repair station for the transmission frequency and for their assistance in checking the VOR system. A logbook entry is required.

Note: Some airborne testing using VOTs is possible by the pilot. An error of ±4° should not be exceeded when testing a VOR system with a VOT. An error in excess of this prevents the use of the aircraft for IFR fight until repairs are made. Aircraft having dual VOR systems where only the antenna is shared may be tested by comparing the output of each system to the other. Tune the VOR receivers to the local ground VOR station. A bearing indication difference of no more than ±4° is permissible.

### Automatic Direction Finder (ADF)

An automatic direction finder (ADF) operates off of a ground signal transmitted from a NDB. Early radio direction finders (RDF) used the same principle. A vertically polarized antenna was used to transmit LF frequency radio waves in the 190 kHz to 535 kHz range. A receiver on the aircraft was tuned to the transmission frequency of the NDB. Using a loop antenna, the direction to (or from) the antenna could be determined by monitoring the strength of the signal received. This was possible because a radio wave striking a loop antenna broadside induces a null signal. When striking it in the plane of the loop, a much stronger signal is induced. The NDB signals were modulated with unique Morse code pulses that enabled the pilot to identify the beacon to which they were navigating.

With RDF systems, a large rigid loop antenna was installed inside the fuselage of the aircraft. The broadside of the antenna was perpendicular to the aircraft’s longitudinal axis. The pilot listened for variations in signal strength of the LF broadcast and maneuvered the aircraft so a gradually increasing null signal was maintained. This took them to the transmitting antenna. When over flown, the null signal gradually faded as the aircraft became farther from the station. The increasing or decreasing strength of the null signal was the only way to determine if the aircraft was flying to or from the NDB. A deviation left or right from the course caused the signal strength to sharply increase due to the loop antenna’s receiving properties.

The ADF improved on this concept. The broadcast frequency range was expanded to include MF up to about 1800 kHz. The heading of the aircraft no longer needed to be changed to locate the broadcast transmission antenna. In early model ADFs, a rotatable antenna was used instead. The antenna rotated to seek the position in which the signal was null. The direction to the broadcast antenna was shown on an azimuth scale of an ADF indicator in the flight deck. This type of instrument is still found in use today. It has a fixed card with 0° always at the top of a non-rotating dial. A pointer indicates the relative bearing to the station. When the indication is 0°, the aircraft is on course to (or from) the station.

As ADF technology progressed, indicators with rotatable azimuth cards became the norm. When an ADF signal is received, the pilot rotates the card so that the present heading is at the top of the scale. This results in the pointer indicating the magnetic bearing to the ADF transmitter. This is more intuitive and consistent with other navigational practices.

In modern ADF systems, an additional antenna is used to remove the ambiguity concerning whether the aircraft is heading to or from the transmitter. It is called a sense antenna. The reception field of the sense antenna is omnidirectional. When combined with the fields of the loop antenna, it forms a field with a single significant null reception area on one side. This is used for tuning and produces an indication in the direction toward the ADF station at all times. The onboard ADF receiver needs only to be tuned to the correct frequency of the broadcast transmitter for the system to work. The loop and sense antenna are normally housed in a single, low profile antenna housing.

Any ground antenna transmitting LF or MF radio waves in range of the aircraft receiver’s tuning capabilities can be used for ADF. This includes those from AM radio stations. Audible identifier tones are loaded on the NDB carrier waves. Typically, a two-character Morse code designator is used. With an AM radio station transmission, the AM broadcast is heard instead of a station identifier code. The frequency for an NDB transmitter is given on an aeronautical chart next to a symbol for the transmitter. The identifying designator is also given.

ADF receivers can be mounted in the flight deck with the controls accessible to the user. This is found on many general aviation aircraft. Alternately, the ADF receiver is mounted in a remote avionics bay with only the control head in the flight deck. Dual ADF receivers are common. ADF information can be displayed on the ADF indicators mentioned or it can be digital. Modern, flat, multipurpose electronic displays usually display the ADF digitally. When ANT is selected on an ADF receiver, the loop antenna is cut out and only the sense antenna is active. This provides better multi-directional reception of broadcasts in the ADF frequency range, such as weather or AWAS broadcasts.

When the best frequency oscillator (BFO) is selected on an ADF receiver/controller, an internal beat frequency oscillator is connected to the IF amplifier inside the ADF receiver. This is used when an NDB does not transmit a modulated signal.

Continued refinements to ADF technology has brought it to its current state. The rotating receiving antenna is replaced by a fixed loop with a ferrite core. This increases sensitivity and allows a smaller antenna to be used. The most modern ADF systems have two loop antennas mounted at 90° to each other. The received signal induces voltage that is sent to two stators in a resolver or goniometer. The goniometer stators induce voltage in a rotor that correlates to the signal of the fixed loops. The rotor is driven by a motor to seek the null. The same motor rotates the pointer in the flight deck indicator to show the relative or magnetic bearing to the station.

Technicians should note that the installation of the ADF antenna is critical to a correct indication since it is a directional device. Calibration with the longitudinal axis of the fuselage or nose of the aircraft is important. A single null reception area must exist in the correct direction. The antenna must be oriented so the ADF indicates station location when the aircraft is flying toward it rather than away. Follow all manufacturer’s instructions.

### Radio Magnetic Indicator (RMI)

To save space in the instrument panel and to consolidate related information into one easy to use location, the radio magnetic indicator (RMI) has been developed. It is widely used. The RMI combines indications from a magnetic compass, VOR, and ADF into one instrument.

The azimuth card of the RMI is rotated by a remotely located flux gate compass. Thus, the magnetic heading of the aircraft is always indicated. The lubber line is usually a marker or triangle at the top of the instrument dial. The VOR receiver drives the solid pointer to indicate the magnetic direction TO a tuned VOR station. When the ADF is tuned to an NDB, the double, or hollow pointer, indicates the magnetic bearing to the NDB.

Since the flux gate compass continuously adjusts the azimuth card so that the aircraft heading is at the top of the instrument, pilot workload is reduced. The pointers indicate where the VOR and ADF transmission stations are located in relationship to where the aircraft is currently positioned. Push buttons allow conversion of either pointer to either ADF or VOR for navigation involving two of one type of station and none of the other.

### Instrument Landing Systems (ILS)

An ILS is used to land an aircraft when visibility is poor. This radio navigation system guides the aircraft down a slope to the touch down area on the runway. Multiple radio transmissions are used that enable an exact approach to landing with an ILS. A localizer is one of the radio transmissions. It is used to provide horizontal guidance to the center line of the runway. A separate glideslope broadcast provides vertical guidance of the aircraft down the proper slope to the touch down point. Compass locator transmissions for outer and middle approach marker beacons aid the pilot in intercepting the approach navigational aid system. Marker beacons provide distance-from-the-runway information. Together, all of these radio signals make an ILS a very accurate and reliable means for landing aircraft.

#### Localizer

The localizer broadcast is a VHF broadcast in the lower range of the VOR frequencies (108 MHz–111.95 MHz) on odd frequencies only. Two modulated signals are produced from a horizontally polarized antenna complex beyond the far end of the approach runway. They create an expanding field that is 2 1 ⁄ 2° wide (about 1,500 feet) 5 miles from the runway. The field tapers to runway width near the landing threshold. The left side of the approach area is filled with a VHF carrier wave modulated with a 90 Hz signal. The right side of the approach contains a 150 MHz modulated signal. The aircraft’s VOR receiver is tuned to the localizer VHF frequency that can be found on published approach plates and aeronautical charts.

The circuitry specific to standard VOR reception is inactive while the receiver uses localizer circuitry and components common to both. The signals received are passed through filters and rectified into DC to drive the course deviation indicator. If the aircraft receives a 150 Hz signal, the CDI of the VOR/ILS display deflects to the left. This indicates that the runway is to the left. The pilot must correct course with a turn to the left. This centers the course deviation indicator on the display and centers the aircraft with the centerline of the runway. If the 90 Hz signal is received by the VOR receiver, the CDI deflects to the right. The pilot must turn toward the right to center the CDI and the aircraft with the runway center line.

#### Glideslope

The vertical guidance required for an aircraft to descend for a landing is provided by the glideslope of the ILS. The glideslope provides vertical guidance for correct angle of descent. Radio signals funnel the aircraft down to the touchdown point on the runway at an angle of approximately 3°. The transmitting glideslope antenna is located off to the side of the approach runway approximately 1,000 feet from the threshold. It transmits in a wedge-like pattern with the field narrowing as it approaches the runway.

The glideslope transmitter antenna is horizontally polarized. The transmitting frequency range is UHF between 329.3 MHz and 335.0 MHz. The frequency is paired to the localizer frequency of the ILS. When the VOR/ILS receiver is tuned for the approach, the glideslope receiver is automatically tuned. Like the localizer, the glideslope transmits two signals, one modulated at 90 Hz and the other modulated at 150 Hz. The aircraft’s glideslope receiver deciphers the signals similar to the method of the localizer receiver. It drives a vertical course deviation indicator known as the glideslope indicator. The glideslope indicator operates identically to the localizer CDI only 90° to it. The VOR/ILS localizer CDI and the glideslope are displayed together on whichever kind of instrumentation is in the aircraft.

The UHF antenna for aircraft reception of the glideslope signals comes in many forms. A single dipole antenna mounted inside the nose of the aircraft is a common option. Antenna manufacturers have also incorporated glideslope reception into the same dipole antenna used for the VHS VOR/ILS localizer reception. Blade type antennas are also used. [Figures 11-114] Figure 11-115 shows a VOR and a glideslope receiver for a GA aircraft ILS.

#### Compass Locators

It is imperative that a pilot be able to intercept the ILS to enable its use. A compass locator is a transmitter designed for this purpose. There is typically one located at the outer marker beacon 4–7 miles from the runway threshold. Another may be located at the middle marker beacon about 3,500 feet from the threshold. The outer marker compass locator is a 25 watt NDB with a range of about 15 miles. It transmits omnidirectional LF radio waves (190 Hz to 535 Hz) keyed with the first two letters of the ILS identifier. The ADF receiver is used to intercept the locator so no additional equipment is required. If a middle marker compass locator is in place, it is similar but is identified with the last two letters of the ILS identifier. Once located, the pilot maneuvers the aircraft to fly down the glidepath to the runway.

#### Marker Beacons

Marker beacons are the final radio transmitters used in the ILS. They transmit signals that indicate the position of the aircraft along the glidepath to the runway. As mentioned, an outer marker beacon transmitter is located 4–7 miles from the threshold. It transmits a 75 MHz carrier wave modulated with a 400 Hz audio tone in a series of dashes. The transmission is very narrow and directed straight up. A marker beacon receiver receives the signal and uses it to light a blue light on the instrument panel. This, plus the oral tone in combination with the localizer and the glideslope indicator, positively locates the aircraft on an approach.

A middle marker beacon is also used. It is located on approach approximately 3,500 feet from the runway. It also transmits at 75 MHz. The middle marker transmission is modulated with a 1300 Hz tone that is a series of dots and dashes so as to not be confused with the all dash tone of the outer marker. When the signal is received, it is used in the receiver to illuminate an amber-colored light on the instrument panel.

Some ILS approaches have an inner marker beacon that transmits a signal modulated with 3000 Hz in a series of dots only. It is placed at the land-or-go-around decision point of the approach close to the runway threshold. If present, the signal when received is used to illuminate a white light on the instrument panel. The three marker beacon lights are usually incorporated into the audio panel of a general aviation aircraft or may exist independently on a larger aircraft. Electronic display aircraft usually incorporate marker lights or indicators close to the glideslope display near attitude director indicator.

ILS radio components can be tested with an ILS test unit. Localizer, glideslope, and marker beacon signals are generated to ensure proper operation of receivers and correct display on flight deck instruments.

### Distance Measuring Equipment (DME)

Many VOR stations are co-located with the military version of the VOR station, which is known as TACAN. When this occurs, the navigation station is known as a VORTAC station. Civilian aircraft make use of one of the TACAN features not originally installed at civilian VOR stations–DME. A DME system calculates the distance from the aircraft to the DME unit at the VORTAC ground station and displays it on the flight deck. It can also display calculated aircraft speed and elapsed time for arrival when the aircraft is traveling to the station.

DME ground stations have subsequently been installed at civilian VORs, as well as in conjunction with ILS localizers. These are known as VOR/DME and ILS/DME or LOC/DME. The latter aid in approach to the runway during landings. The DME system consists of an airborne DME transceiver, display, and antenna, as well as the ground based DME unit and its antenna.

The DME is useful because with the bearing (from the VOR) and the distance to a known point (the DME antenna at the VOR), a pilot can positively identify the location of the aircraft. DME operates in the UHF frequency range from 962 MHz to 1213 MHz. A carrier signal transmitted from point directly beneath the aircraft is shorter. Some modern DMEs are equipped to calculate this ground distance and display it.

### Area Navigation (RNAV)

Area navigation (RNA V) is a general term used to describe the navigation from point A to point B without direct over flight of navigational aids, such as VOR stations or ADF non-directional beacons. It includes VORTAC and VOR/DME based systems, as well as systems of RNA V based around LORAN, GPS, INS, and the FMS of transport category aircraft. However, until recently, the term RNA V was most commonly used to describe the area navigation or the process of direct flight from point A to point B using VORTAC and VOR/DME based references which are discussed in this section.

All RNA V systems make use of waypoints. A waypoint is a designated geographical location or point used for route definition or progress-reporting purposes. It can be defined or described by using latitude/longitude grid coordinates or, in the case of VOR based RNA V , described as a point on a VOR radial followed by that point’s distance from the VOR station (i.e., 200/25 means a point 25 nautical miles from the VOR station on the 200° radial).

Figure 11-123 illustrates an RNA V route of flight from airport A to airport B. The VOR/DME and VORTAC stations shown are used to create phantom waypoints that are overflown rather than the actual stations. This allows a more direct route to be taken. The phantom waypoints are entered into the RNA V course-line computer (CLC) as a radial and distance number pair. The computer creates the waypoints and causes the aircraft’s CDI to operate as though they are actual VOR stations. A mode switch allows the choice between standard VOR navigation and RNA V .

VOR based RNA V uses the VOR receiver, antenna, and VOR display equipment, such as the CDI. The computer in the RNA V unit uses basic geometry and trigonometry calculations to produce heading, speed, and time readouts for each waypoint. VOR stations need to be within line-of sight and operational range from the aircraft for RNA V use.

RNA V has increased in flexibility with the development of GPS. Integration of GPS data into a planned VOR RNA V flight plan is possible as is GPS route planning without the use of any VOR stations.

### Radar Beacon Transponder

A radar beacon transponder, or simply, a transponder, provides positive identification and location of an aircraft on the radar screens of ATC. For each aircraft equipped with an altitude encoder, the transponder also provides the pressure altitude of the aircraft to be displayed adjacent to the on-screen blip that represents the aircraft.

Radar capabilities at airports vary. Generally, two types of radar are used by air traffic control (ATC). The primary radar transmits directional UHF or SHF radio waves sequentially in all directions. When the radio waves encounter an aircraft, part of those waves reflect back to a ground antenna. Calculations are made in a receiver to determine the direction and distance of the aircraft from the transmitter. A blip or target representing the aircraft is displayed on a radar screen also known as a plan position indicator (PPI). The azimuth direction and scaled distance from the tower are presented giving controllers a two dimensional fix on the aircraft. A secondary surveillance radar (SSR) is used by ATC to verify the aircraft’s position and to add the third dimension of altitude to its location. SSD radar transmits coded pulse trains that are received by the transponder on board the aircraft. Mode 3/A pulses, as they are known, aid in confirming the location of the aircraft. When verbal communication is established with ATC, a pilot is instructed to select one of 4,096 discrete codes on the transponder. These are digital octal codes. The ground station transmits a pulse of energy at 1030 MHz and the transponder transmits a reply with the assigned code attached at 1090 MHz. This confirms the aircraft’s location typically by altering its target symbol on the radar screen. As the screen may be filled with many confirmed aircraft, ATC can also ask the pilot to ident. By pressing the IDENT button on the transponder, it transmits in such a way that the aircraft’s target symbol is highlighted on the PPI to be distinguishable.

To gain altitude clarification, the transponder control must be placed in the ALT or Mode C position. The signal transmitted back to ATC in response to pulse interrogation is then modified with a code that places the pressure altitude of the aircraft next to the target symbol on the radar screen. The transponder gets the pressure altitude of the aircraft from an altitude encoder that is electrically connected to the transponder. Typical aircraft transponder antennas are illustrated in Figure 11-127.

The ATC/aircraft transponder system described is known as Air Traffic Control Radar Beacon System (ATCRBS). To increase safety, Mode S altitude response has been developed. With Mode S, each aircraft is pre-assigned a unique identity code that displays along with its pressure altitude on ATC radar when the transponder responds to SSR interrogation. Since no other aircraft respond with this code, the chance of two pilots selecting the same response code on the transponder is eliminated. A modern flight data processor computer (FDP) assigns the beacon code and searches flight plan data for useful information to be displayed on screen next to the target in a data block for each aircraft.

Mode S is sometimes referred to as mode select. It is a data packet protocol that is also used in onboard collision avoidance systems. When used by ATC, Mode S interrogates one aircraft at a time. Transponder workload is reduced by not having to respond to all interrogations in an airspace.

Additionally, location information is more accurate with Mode S. A single reply in which the phase of the transponder reply is used to calculate position, called monopulse, is sufficient to locate the aircraft. Mode S also contains capacity for a wider variety of information exchange that is untapped potential for the future. At the same time, compatibility with older radar and transponder technology has been maintained.

#### Transponder Tests & Inspections

Title 14 of the Code of Federal Regulations (CFR) part 91, section 91.413 states that all transponders on aircraft flown into controlled airspace are required to be inspected and tested in accordance with 14 CFR part 43, Appendix F, every 24 calendar months. Installation or maintenance that may introduce a transponder error is also cause for inspection and test in accordance with Appendix F. Only an appropriately rated repair station, the aircraft manufacturer (if it installed transponder), and holders of a continuous airworthy program are approved to conduct the procedures. As with many radio-electronic devices, test equipment exists to test airworthy operation of a transponder.

Operating a transponder in a hangar or on the ramp does not immunize it from interrogation and reply. Transmission of certain codes reserved for emergencies or military activity must be avoided. The procedure to select a code during ground operation is to do so with the transponder in the OFF or STANDBY mode to avoid inadvertent transmission. Code 0000 is reserved for military use and is a transmittable code. Code 7500 is used in a hijack situation and 7600 and 7700 are also reserved for emergency use. Even the inadvertent transmission of code 1200 reserved for VFR flight not under ATC direction could result in evasion action. All signals received from a radar beacon transponder are taken seriously by ATC.

#### Altitude Encoders

Altitude encoders convert the aircraft’s pressure altitude into a code sent by the transponder to ATC. Increments of 100 feet are usually reported. Encoders have varied over the years. Some are built into the altimeter instrument used in the instrument panel and connected by wires to the transponder. Others are mounted out of sight on an avionics rack or similar out of the way place. These are known as blind encoders. On transport category aircraft, the altitude encoder may be a large black box with a static line connection to an internal aneroid. Modern general aviation encoders are smaller and more lightweight, but still often feature an internal aneroid and static line connection. Some encoders use microtransistors and are completely solid-state including the pressure sensing device from which the altitude is derived. No static port connection is required. Data exchange with GPS and other systems is becoming common.

When a transponder selector is set on ALT, the digital pulse message sent in response to the secondary surveillance radar interrogation becomes the digital representation of the pressure altitude of the aircraft. There are 1280 altitude codes, one for each 100 feet of altitude between 1200 feet mean sea level (MSL) and 126,700 feet MSL. Each altitude increment is assigned a code. While these would be 1280 of the same codes used for location and IDENT, the Mode C (or S) interrogation deactivates the 4096 location codes and causes the encoder to become active. The correct altitude code is sent to the transponder that replies to the interrogation. The SSR receiver recognized this as a response to a Mode C (or S) interrogation and interprets the code as altitude code.

### Collision Avoidance Systems

The ever increasing volume of air traffic has caused a corresponding increase in concern over collision avoidance. Ground-based radar, traffic control, and visual vigilance are no longer adequate in today’s increasingly crowded skies. Onboard collision avoidance equipment, long a staple in larger aircraft, is now common in general aviation aircraft.

New applications of electronic technology combined with lower costs make this possible.

#### Traffic Collision Avoidance Systems (TCAS)

Traffic collision avoidance systems (TCAS) are transponder based air-to-air traffic monitoring and alerting systems. There are two classes of TCAS. TCAS I was developed to accommodate the general aviation community and regional airlines. This system identifies traffic in a 35–40 mile range of the aircraft and issues Traffic Advisories (TA) to assist pilots in visual acquisition of intruder aircraft. TCAS I is mandated on aircraft with 10 to 30 seats.

TCAS II is a more sophisticated system. It is required internationally in aircraft with more than 30 seats or weighing more than 15,000 kg. TCAS II provides the information of TCAS I, but also analyzes the projected flightpath of approaching aircraft. If a collision or near miss is imminent, the TCAS II computer issues a Resolution Advisory (RA). This is an aural command to the pilot to take a specific evasive action (i.e., DESCEND). The computer is programmed such that the pilot in the encroaching aircraft receives an RA for evasive action in the opposite direction (if it is TCAS II equipped).

The transponder of an aircraft with TCAS is able to interrogate the transponders of other aircraft nearby using SSR technology (Mode C and Mode S). This is done with a 1030 MHz signal. Interrogated aircraft transponders reply with an encoded 1090 MHz signal that allows the TCAS computer to display the position and altitude of each aircraft. Should the aircraft come within the horizontal or vertical distances shown in Figure 11-131 , an audible TA is announced. The pilot must decide whether to take action and what action to take. TCAS II equipped aircraft use continuous reply information to analyze the speed and trajectory of target aircraft in close proximity. If a collision is calculated to be imminent, an RA is issued.

TCAS target aircraft are displayed on a screen on the flight deck. Different colors and shapes are used to depict approaching aircraft depending on the imminent threat level. Since RAs are currently limited to vertical evasive maneuvers, some stand-alone TCAS displays are electronic vertical speed indicators. Most aircraft use some version of an electronic HSI on a navigational screen or page to display TCAS information. A multifunction display may depict TCAS and weather radar information on the same screen. A TCAS control panel and computer are required to work with a compatible transponder and its antenna(s). Interface with EFIS or other previously installed or selected display(s) is also required.

TCAS may be referred to as airborne collision avoidance system (ACAS), which is the international name for the same system. TCAS II with the latest revisions is known as Version 7. The accuracy and reliability of this TCAS information is such that pilots are required to follow a TCAS RA over an ATC command.

#### ADS-B

Collision avoidance is a significant part of the FAA’s NextGen plan for transforming the National Airspace System (NAS). Increasing the number of aircraft using the same quantity of airspace and ground facilities requires the implementation of new technologies to maintain a high level of performance and safety. The successful proliferation of global navigation satellite systems (GNSS), such as GPS, has led to the development of a collision avoidance system known as Automatic Dependent Surveillance-Broadcast (ADS-B). ADS-B is an integral part of NextGen program. The implementation of its ground and airborne infrastructure is currently underway. ADS-B is active in parts of the United States and around the world.

ADS-B is considered in two segments: ADS-B OUT and ADS-B IN. ADS-B OUT combines the positioning information available from a GPS receiver with on-board flight status information, i.e., location including altitude, velocity, and time. It then broadcasts this information to other ADS-B equipped aircraft and ground stations.

Two different frequencies are used to carry these broadcasts with data link capability. The first is an expanded use of the 1090 MHz Mode-S transponder protocol known as 1090 ES. The second, largely being introduced as a new broadband solution for general aviation implementation of ADS-B, is at 978 MHz. A 978 universal access transceiver (UAT) is used to accomplish this. An omni-directional antenna is required in addition to the GPS antenna and receiver. Airborne receivers of an ADS-B use the information to plot the location and movement of the transmitting aircraft on a flight deck display similar to TCAS.

Inexpensive ground stations (compared to radar) are constructed in remote and obstructed areas to proliferate ADS-B. Ground stations share information from airborne ADS-Bs with other ground stations that are part of the air traffic management system (ATMS). Data is transferred with no need for human acknowledgement. Microwave and satellite transmissions are used to link the network.

For traffic separation and control, ADS-B has several advantages over conventional ground-based radar. The first is the entire airspace can be covered with a much lower expense. The aging ATC radar system that is in place is expensive to maintain and replace. Additionally, ADS-B provides more accurate information since the vector state is generated from the aircraft with the help of GPS satellites. Weather is a greatly reduced factor with ADS-B. Ultra-high frequency GPS transmissions are not affected. Increased positioning accuracy allows for higher density traffic flow and landing approaches, an obvious requirement to operate more aircraft in and out of the same number of facilities. The higher degree of control available also enables routing for fewer weather delays and optimal fuel burn rates. Collision avoidance is expanded to include runway incursion from other aircraft and support vehicles on the surface of an airport.

ADS-B IN offers features not available in TCAS. Equipped aircraft are able to receive abundant data to enhance situational awareness. Traffic information services-broadcast (TIS-B) supply traffic information from non-ADS-B aircraft and ADS-B aircraft on a different frequency. Ground radar monitoring of surface targets, and any traffic data in the linked network of ground stations is sent via ADS-B IN to the flight deck. This provides a more complete picture than air-to-air only collision avoidance. Flight information services-broadcast (FIS-B) is also received by ADS-B IN. Weather text and graphics, ATIS information, and NOTAMs are able to be received in aircraft that have 987 UAT capability.

ADS-B test units are available for trained maintenance personnel to verify proper operation of ADS-B equipment. This is critical since close tolerance of air traffic separation depends on accurate data from each aircraft and throughout all components of the ADS-B system.

### Radio Altimeter

A radio altimeter, or radar altimeter, is used to measure the distance from the aircraft to the terrain directly beneath it. It is used primarily during instrument approach and low level or night flight below 2,500 feet. The radio altimeter supplies the primary altitude information for landing decision height. It incorporates an adjustable altitude bug that creates a visual or aural warning to the pilot when the aircraft reaches that altitude. Typically, the pilot will abort a landing if the decision height is reached and the runway is not visible.

Using a transceiver and a directional antenna, a radio altimeter broadcasts a carrier wave at 4.3 GHz from the aircraft directly toward the ground. The wave is frequency modulated at 50 MHz and travels at a known speed. It strikes surface features and bounces back toward the aircraft where a second antenna receives the return signal. The transceiver processes the signal by measuring the elapsed time the signal traveled and the frequency modulation that occurred. The display indicates height above the terrain also known as above ground level (AGL). A radar altimeter is more accurate and responsive than an air pressure altimeter for AGL information at low altitudes. The transceiver is usually located remotely from the indicator. Multifunctional and glass flight deck displays typically integrate decision height awareness from the radar altimeter as a digital number displayed on the screen with a bug, light, or color change used to indicate when that altitude is reached.

Large aircraft may incorporate radio altimeter information into a ground proximity warning system (GPWS) which aurally alerts the crew of potentially dangerous proximity to the terrain below the aircraft. A decision height (DH) window displays the radar altitude on the EADI in Figure 11-141 .

### Weather Radar

There are three common types of weather aids used in an aircraft flight deck that are often referred to as weather radar:

1. Actual on-board radar for detecting and displaying weather activity;

2. Lightning detectors; and 3. Satellite or other source weather radar information that is uploaded to the aircraft from an outside source.

On-board weather radar systems can be found in aircraft of all sizes. They function similar to ATC primary radar except the radio waves bounce off of precipitation instead of aircraft. Dense precipitation creates a stronger return than light precipitation. The on-board weather radar receiver is set up to depict heavy returns as red, medium returns as yellow and light returns as green on a display in the flight deck. Clouds do not create a return. Magenta is reserved to depict intense or extreme precipitation or turbulence. Some aircraft have a dedicated weather radar screen. Most modern aircraft integrate weather radar display into the navigation display(s). Figure 11-142 illustrates weather radar displays found on aircraft.

Radio waves used in weather radar systems are in the SHF range such as 5.44 GHz or 9.375 GHz. They are transmitted forward of the aircraft from a directional antenna usually located behind a non-metallic nose cone. Pulses of approximately 1 micro-second in length are transmitted. A duplexer in the radar transceiver switches the antenna to receive for about 2,500 micro seconds after a pulse is transmitted to receive and process any returns. This cycle repeats and the receiver circuitry builds a two dimensional image of precipitation for display. Gain adjustments control the range of the radar. A control panel facilitates this and other adjustments.

Severe turbulence, windshear, and hail are of major concern to the pilot. While hail provides a return on weather radar, windshear and turbulence must be interpreted from the movement of any precipitation that is detected. An alert is annunciated if this condition occurs on a weather radar system so equipped. Dry air turbulence is not detectable. Ground clutter must also be attenuated when the radar sweep includes any terrain features. The control panel facilitates this.

Special precautions must be followed by the technician during maintenance and operation of weather radar systems. The radome covering the antenna must only be painted with approved paint to allow the radio signals to pass unobstructed. Many radomes also contain grounding strips to conduct lightning strikes and static away from the dome.

When operating the radar, it is important to follow all manufacturer instructions. Physical harm is possible from the high energy radiation emitted, especially to the eyes and testes. Do not look into the antenna of a transmitting radar.

Operation of the radar should not occur in hangars unless special radio wave absorption material is used. Additionally, operation of radar should not take place while the radar is pointed toward a building or when refueling takes place.

Radar units should be maintained and operated only by Lightning detection is a second reliable means for identifying potentially dangerous weather. Lightning gives off its own electromagnetic signal. The azimuth of a lightning strike can be calculated by a receiver using a loop type antenna such as that used in ADF. Some lightning detectors make use of the ADF antenna. The range of the lightning strike is closely associated with its intensity. Intense strikes are plotted as being close to the aircraft.

Stormscope is a proprietary name often associated with lightning detectors. There are others that work in a similar manner. A dedicated display plots the location of each strike within a 200 mile range with a small mark on the screen. As time progresses, the marks may change color to indicate their age. Nonetheless, a number of lightning strikes in a small area indicates a storm cell, and the pilot can navigate around it. Lightning strikes can also be plotted on a multifunctional navigation display.

A third type of weather radar is becoming more common in all classes of aircraft. Through the use of orbiting satellite systems and/or ground up-links, such as described with ADS-B IN, weather information can be sent to an aircraft in flight virtually anywhere in the world. This includes text data as well as real-time radar information for overlay on an aircraft’s navigational display(s). Weather radar data produced remotely and sent to the aircraft is refined through consolidation of various radar views from different angles and satellite imagery. This produces more accurate depictions of actual weather conditions. Terrain databases are integrated to eliminate ground clutter. Supplemental data includes the entire range of intelligence available from the National Weather Service (NWS) and the National Oceanographic and Atmospheric Administration (NOAA). Figure 11-146 illustrates a plain language weather summary received in an aircraft along with a list of other weather information available through satellite or ground link weather information services.

As mentioned, to receive an ADS-B weather signal, a 1090 ES or 970 UAT transceiver with associated antenna needs to be installed on board the aircraft. Satellite weather services are received by an antenna matched to the frequency of the service. Receivers are typically located remotely and interfaced with existing navigational and multifunction displays. Handheld GPS units also may have satellite weather capability.

### Emergency Locator Transmitter (ELT)

An emergency locator transmitter (ELT) is an independent battery powered transmitter activated by the excessive G-forces experienced during a crash. It transmits a digital signal every 50 seconds on a frequency of 406.025 MHz at 5 watts for at least 24 hours. The signal is received anywhere in the world by satellites in the Cospas-Sarsat satellite system. Two types of satellites, low earth orbiting satellites (LEOSATs) and geostationary satellites (GEOSATs), are used with different, complimentary capability. The signal is partially processed and stored in the satellites and then relayed to ground stations known as local user terminals (LUTs). Further deciphering of a signal takes place at the LUTs, and appropriate search and rescue operations are notified through mission control centers (MCCs) set up for this purpose.

Note: Maritime vessel emergency locating beacons (EPIRBs) and personal locator beacons (PLBs) use the exact same system. The United States portion of the Cospas-Sarsat system is maintained and operated by NOAA. Figure 11-148 illustrates the basic components in the Cospas-Sarsat system.

ELTs are required to be installed in aircraft according to FAR 91.207. This encompasses most general aviation aircraft not operating under parts 135 or 121. ELTs must be inspected within 12 months of previous inspection for proper installation, battery corrosion, operation of the controls and crash sensor, and the presence of a sufficient signal at the antenna. Built-in test equipment facilitates testing without transmission of an emergency signal. The remainder of the inspection is visual. Technicians are cautioned to not activate the ELT and transmit an emergency distress signal. Inspection must be recorded in maintenance records including the new expiration date of the battery. This must also be recorded on ELTs are typically installed as far aft in the fuselage of an aircraft as is practicable just forward of the empennage. The built-in G-force sensor is aligned with the longitudinal axis of the aircraft. Helicopter ELTs may be located elsewhere on the airframe. They are equipped with multidirectional activation devices. Follow ELT and airframe manufacturer’s instructions for proper installation, inspection, and maintenance of all ELTs.

Figure 11-149 illustrates ELTs mounted locations.

Use of Doppler technology enables the origin of the 406 MHz ELT signal to be calculated within 2 to 5 kilometers.

Second generation 406 MHz ELT digital signals are loaded with GPS location coordinates from a receiver inside the ELT unit or integrated from an outside unit. This reduces the location accuracy of the crash site to within 100 meters.

The digital signal is also loaded with unique registration information. It identifies the aircraft, the owner, and contact information, etc. When a signal is received, this is used to immediately research the validity of the alert to ensure it is a true emergency transmission so that rescue resources are ELTs with automatic G-force activation mounted in aircraft are easily removable. They often contain a portable antenna so that crash victims may leave the site and carry the operating ELT with them. A flight deck mounted panel is required to alert the pilot if the ELT is activated. It also allows the ELT to be armed, tested, and manually activated if needed.

Modern ELTs may also transmit a signal on 121.5 MHz. This is an analog transmission that can be used for homing. Prior to 2009, 121.5 MHz was a worldwide emergency frequency monitored by the Cospas-Sarsat satellites. However, it has been replaced by the 406 MHz standard. Transmissions on 121.5 MHz are no longer received and relayed via satellite.

The use of a 406 MHz ELT has not been mandated by the FAA. An older 121.5 MHz ELT satisfies the requirements of FAR Part 91.207 in all except new aircraft. Thousands of aircraft registered in the United States remain equipped with ELTs that transmit a .75 watt analog 121.5 MHz emergency signal when activated. The 121.5 MHz frequency is still an emergency frequency and is not monitored by over-flying aircraft and control towers.

Technicians are required to perform an inspection/test of 121.5 MHz ELTs within 12 months of the previous one and inspect for the same integrity as required for the 406 MHz ELTs mentioned above. However, older ELTs often lack the built-in test circuitry of modern ELTs certified to TSO C-126. Therefore, a true operational test may include activating the signal. This can be done by removing the antenna and installing a dummy load. Any activation of an ELT signal is required to only be done between the top of each hour and 5 minutes after the hour. The duration of activation must be no longer than three audible sweeps. Contact of the local control tower or flight service station before testing is recommended.

It must be noted that older 121.5 MHz analog signal ELTs often also transmit an emergency signal on a frequency of 243.0 MHz. This has long been the military emergency frequency. Its use is being phased out in favor of digital ELT signals and satellite monitoring. Testing the functionality of a 121.5 MHz transmitter should be accomplished per manufacturer’s instructions. Improvements in coverage, location accuracy, identification of false alerts, and shortened response times are so significant with 406 MHz ELTs, they are currently the service standard worldwide.

#### Testing Considerations for 406 MHz ELTs

Care should be taken to prevent accidentally triggering a SAR (search and rescue) response. Accidental activation of an ELT will generate an emergency signal that cannot be distinguished from that of an actual emergency and could lead to expensive and frustrating searches. Moreover, the unwarranted ELT signal could tie up the emergency frequencies such that a genuine emergency signal would not be picked up. In addition, if an ELT signal is transmitted on or near an airport, it may render some radio communications channels unusable.

Regardless of where the ELT is, or the duration of activation, a 406 MHz beacon broadcast will be detected by at least one Geostationary Local User Terminal (GEOLUT) and possibly every Low Earth Orbit Local User Terminal (LEOLUT) in the Cospas-Sarsat System. Alert messages will be routed to every Mission Control Center (MCC) in the Cospas-Sarsat System for coordination around the world and a response will be made (unless prior coordination is made with Cospas-Sarsat and local authorities).

Direct connect testing is preferred to prevent inadvertent activation of the SAR response system. Over-air testing should always be avoided if possible. Use of an antenna boot or a direct connection from test equipment to the antenna port is preferred. Testing an ELT system in a metal hangar will not guarantee the radiated signal will not be detected by the Cospas-Sarsat System. Technicians testing ELT devices in a hangar should treat the test as if they were testing outside.

When testing an ELT, a 50-ohm dummy load or antenna boot should be used to prevent the signal from being radiated into space. The signal must be attenuated to less than -51 dBW (a power flux density of -37.4 dB (W/m2) or a field intensity of -11.6 dB (V/m).

If over-air testing must be accomplished, technicians should carefully follow Cospas-Sarsat instructions and use the built-in test message on the ELT device. The ELT test message is different from messages transmitted during an emergency, but is still detectable by the Cospas-Sarsat System. Cospas-Sarsat should be contacted prior to performing over-air testing. Cospas-Sarsat can be contacted at www.cospas-sarsat.int/en/. If over-air testing must be accomplished, the local air traffic control (ATC) facility should be contacted in advance.

Follow test set instructions or place the test set a minimum of 12 meters, (39.4 feet) from the ELT antenna. Test in each mode and frequency the ELT unit transmits.

#### 406 MHz Testing

Verify the device is outputting a signal of not less than 17 dBm (50 mW) and not greater than 26 dBm (400 mW).

Verify the device is transmitting on the correct frequency. This can be done by running the ELT self-test and detecting the signal with an ELT test set. Receiving and decoding a test message is an indication the unit is transmitting on a correct frequency.

Using appropriate test equipment and shielding, note the ELT code transmitted and verify that the ELT code is registered with Cospas-Sarsat. The testing technician or aircraft owner should verify the information on file with Cospas-Sarsat is accurate and up to date.

Determine that the ELT aural indicator can be heard in the flight deck with the aircraft engine(s) off, and that the visual indicator can be seen from the crew’s normal sitting position. If possible, this should be performed in a way that will prevent a SAR response (e.g., with a dummy load installed).

Perform an operational check of the g switch. This should be performed in a way that will prevent a SAR response (e.g., with a dummy load installed). Replace if the g switch fails to activate.

Ensure all cables except the 406 MHz transmitter output are reconnected. Ensure the 406 MHz transmitter is connected to a test set if possible. Activate the ELT (use the remote switch if installed), and determine if the system is radiating a strong 406 MHz signal. Ensure the system is reset if necessary.

If equipped with a water-activated circuit, connect the ELT to a test set if possible. Activate the ELT by shorting the water-sensing leads and determine if the system is radiating a strong 406 MHz signal. Ensure the system is reset if necessary.

### Long Range Aid to Navigation System (LORAN)

Long range aid to navigation system (LORAN) is a type of RNA V that is no longer available in the United States. It was developed during World War II, and the most recent edition, LORAN-C, has been very useful and accurate to aviators as well as maritime sailors. LORAN uses radio wave pulses from a series of towers and an on-board receiver/computer to positively locate an aircraft amid the tower network. There are twelve LORAN transmitter tower “chains” constructed across North America. Each chain has a master transmitter tower and a handful of secondary towers. All broadcasts from the transmitters are at the same frequency, 100 KHz. Therefore, a LORAN receiver does not need to be tuned. Being in the low frequency range, the LORAN transmissions travel long distances and provide good coverage from a small number of stations.

Precisely-timed, synchronized pulse signals are transmitted from the towers in a chain. The LORAN receiver measures the time to receive the pulses from the master tower and two other towers in the chain. It calculates the aircraft’s position based on the intersection of parabolic curves representing elapsed signal times from each of these known points.

The accuracy and proliferation of GPS navigation has caused the U.S. Government to cease support for the LORAN navigation system citing redundancy and expense of operating the towers as reasons. Panel-mounted LORAN navigation units will likely be removed and replaced by GPS units in aircraft that have not already done so.

### Global Positioning System (GPS)

Global positioning system (GPS) navigation is the fastest growing type of navigation in aviation. It is accomplished through the use of NA VSTAR satellites set and maintained in orbit around the earth by the U.S. Government. Continuous coded transmissions from the satellites facilitate locating the position of an aircraft equipped with a GPS receiver with extreme accuracy. GPS can be utilized on its own for en route navigation, or it can be integrated into other navigation systems, such as VOR/RNA V , inertial reference, or flight management systems.

There are three segments of GPS: the space segment, the control segment, and the user segment. Aircraft technicians are only involved with user segment equipment such as GPS receivers, displays, and antennas.

Twenty-four satellites (21 active, 3 spares) in six separate planes of orbit 12,625 miles above the planet comprise what is known as the space segment of the GPS system. The satellites are positioned such that in any place on earth at any one time, at least four will be a minimum of 15° above the horizon. Typically, between five and eight satellites are in view. Two signals loaded with digitally coded information are transmitted from each satellite. The L1 channel transmission on a 1575.42 MHz carrier frequency is used in civilian aviation. Satellite identification, position, and time are conveyed to the aircraft GPS receiver on this digitally modulated signal along with status and other information. An L2 channel 1227.60 MHz transmission is used by the military.

The amount of time it takes for signals to reach the aircraft GPS receiver from transmitting satellites is combined with each satellite’s exact location to calculate the position of an aircraft. The control segment of the GPS monitors each satellite to ensure its location and time are precise. This control is accomplished with five ground-based receiving stations, a master control station, and three transmitting antennas. The receiving stations forward status information received from the satellites to the master control station. Calculations are made, and corrective instructions are sent to the satellites via the transmitters.

The user segment of the GPS is comprised of the thousands of receivers installed in aircraft as well as every other receiver that uses the GPS transmissions. Specifically, for the aircraft technician, the user section consists of a control panel/display, the GPS receiver circuitry, and an antenna. The control, display and receiver are usually located in a single unit which also may include VOR/ILS circuitry and a VHF communications transceiver. GPS intelligence is integrated into the multifunctional displays of glass flight deck aircraft.

The GPS receiver measures the time it takes for a signal to arrive from three transmitting satellites. Since radio waves travel at 186,000 miles per second, the distance to each satellite can be calculated. The intersection of these ranges provides a two dimensional position of the aircraft. It is expressed in latitude/longitude coordinates. By incorporating the distance to a fourth satellite, the altitude above the surface of the earth can be calculated as well. This results in a three dimensional fix. Additional satellite inputs refine the accuracy of the position.

Having deciphered the position of the aircraft, the GPS unit processes many useful navigational outputs such as speed, direction, bearing to a waypoint, distance traveled, time of arrival, and more. These can be selected to display for use. Waypoints can be entered and stored in the unit’s memory. Terrain features, airport data, VOR/RNA V and approach information, communication frequencies, and more can also be loaded into a GPS unit. Most modern units come with moving map display capability.

A main benefit of GPS use is immunity from service disruption due to weather. Errors are introduced while the carrier waves travel through the ionosphere; however, these are corrected and kept to a minimum. GPS is also relatively inexpensive. GPS receivers for IFR navigation in aircraft must be built to TSO-129A. This raises the price above that of handheld units used for hiking or in an automobile. But the overall cost of GPS is low due to its small infrastructure. Most of the inherent accuracy is built into the space and control segments permitting reliable positioning with inexpensive user equipment.

The accuracy of current GPS is within 20 meters horizontally and a bit more vertically. This is sufficient for en route navigation with greater accuracy than required. However, departures and approaches require more stringent accuracy. Integration of the wide area augmentation system (WAAS) improves GPS accuracy to within 7.6 meters and is discussed below. The future of GPS calls for additional accuracy by adding two new transmissions from each satellite. An L2C channel is for general use in non-safety critical application. An aviation dedicated L5 channel provides the accuracy required for category I, II, and III landings. It enables the NextGen NAS plan along with ADS-B.

#### Wide Area Augmentation System (WAAS)

To increase the accuracy of GPS for aircraft navigation, the wide area augmentation system (WAAS) was developed. It consists of approximately 25 precisely surveyed ground stations that receive GPS signals and ultimately transmit correction information to the aircraft. An overview of WAAS components and its operation is shown in Figure 11-154 .

WAAS ground stations receive GPS signals and forward position errors to two master ground stations. Time and location information is analyzed, and correction instructions are sent to communication satellites in geostationary orbit over the NAS. The satellites broadcast GPS-like signals that WAAS enabled GPS receivers use to correct position information received from GPS satellites.

A WAAS-enabled GPS receiver is required to use the wide area augmentation system. If equipped, an aircraft qualifies to perform precision approaches into thousands of airports without any ground-based approach equipment. Separation minimums are also able to be reduced between aircraft that are WAAS equipped. The WAAS system is known to reduce position errors to 1–3 meters laterally and vertically.

## 2. 中文翻译

在航空的早期，罗盘、地图和推测领航是仅有的导航工具。如果天气使飞行员看不到下方地形，这些手段只能提供勉强的一点安心。地面上的人通过语音无线电告知飞行员已听到飞机从头顶飞过，这已预示了电子导航设备所能提供的东西。要使航空真正成为一种安全、可靠、稳定的运输方式，就必须研制出某种导航系统。

早期的飞行仪表在当地面被云遮蔽时对飞行帮助很大。飞机在飞向目的地的途中，需要导航设备指示它在陆地上方的位置。20 世纪 30 至 40 年代使用过一种低频四航道无线电指向系统。机场和选定的导航航路点播发两种莫尔斯电码信号，各有其作用范围和信号图形。飞行员把接收机调到播发频率，并按某种定向图形飞行，直到两种信号都以逐渐增强的强度被收到。当飞机正好位于播发区域上空时，两种信号会合成为一个音量最大的混合音。自此起步，无线电导航设备不断得到大量改进。

无线电导航设备向飞行员提供维持或提高飞行安全的信息。与通信电台一样，导航设备属于航空电子装置，其修理必须由经过培训的技术人员在认证维修站进行。不过，电子组件及其天线、显示器和任何其他外围设备的安装、维护与正常工作，都是机体技师的责任。

### 甚高频全向信标（VOR）导航系统

历史最悠久、最有用的导航设备之一是甚高频全向信标（VOR）导航系统。典型系统的四个主要部件是：接收机、目视指示器、频率选择器（控制器或控制面板）和天线。该系统建于二战之后，至今仍在使用。它由成千上万个陆基发射台（即 VOR 台）组成，与机载无线电接收设备通信。许多 VOR 台沿航路设置。维克多航路系统就是围绕 VOR 导航系统建立的。机场也设有地面 VOR 发射装置，称为 TVOR（终端 VOR）。美军有一种称为 TACAN 的导航系统，其工作方式与 VOR 类似。有时 VOR 与 TACAN 发射台设在同一地点，这样的台站称为 VORTAC。

所有 VOR、TVOR 和 VORTAC 台的位置都标在航图上，同时标出台名、机载接收机使用该台时必须调到的频率，以及该台的莫尔斯电码代号。有些 VOR 还在一个单独频率上播发语音识别信号，该频率也标注在航图上。

VOR 使用甚高频无线电波（108–117.95 MHz），相邻频道间隔 50 kHz。这使大气干扰降到最低，但也使 VOR 只能视距使用。接收 VOR 甚高频电波通常采用 V 形、水平极化的双极天线。其他型式的天线也经过认证。安装位置应遵照制造商的说明。

VOR 发射机产生的信号从该台向 360° 传播，飞机借助机载 VOR 接收机和显示仪表，利用它飞向或飞离该台。飞行员无需按某种图形飞行去切入 VOR 台信号，因为信号向各个方向传播。只要飞机在地面台的覆盖范围内，无论飞机朝哪个方向飞行，都能收到这些电波。

VOR 发射机产生两种信号，机载接收机用它们确定飞机相对地面台的位置。一种是基准信号。第二种由可变信号经电子旋转产生。可变信号在磁北方向与基准信号同相，旋转到 180° 时相位差逐渐增大。继续旋转到 360°（0°）时，两信号逐渐趋于同相，直到在磁北方向再次同相。机载接收机解出相位差，从而确定飞机相对 VOR 地面台的方位（以度表示）。

大多数飞机装有两套 VOR 接收机。有时 VOR 接收机与甚高频通信收发机同属一个航空电子组件，这类设备称为 NAV/COM 电台。由于两者的频段相邻，内部元件是共用的。

大型飞机可能装有两套双接收机，甚至两副天线。通常选择一部接收机使用，另一部则调到航路上将要遇到的下一个 VOR 台的频率。设备设有在 NAV 1 与 NAV 2 之间转换的装置，也设有选择工作频率或备用频率的开关。VOR 接收机也常与仪表着陆系统（ILS）接收机和下滑道接收机组合在一起。

VOR 接收机解算相对产生信号的 VOR 台的方位（以度表示，向台或背台）。它还产生直流电压，驱动显示器指示相对所选台站预定航向中心线的偏差。此外，接收机还判定飞机是飞向还是飞离 VOR 台。这些信息可以在各种仪表上以多种不同方式显示。较老的飞机常装有专门显示 VOR 信息的 VOR 指示表，这种表也称为全向方位选择器（OBS）或航向偏差指示器（CDI）。CDI 的线性指示器基本保持垂直，但在仪表盘面的刻度上左右移动，以显示偏离航向的程度。每一刻度代表 2°。OBS 旋钮转动方位环。当处于 VOR 覆盖范围内时，飞行员转动 OBS 直至航向偏差指示器居中。对飞机的每一个位置，OBS 都可转到两个使 CDI 居中的位置。其中一个使指示表“TO”（向台）窗口出现箭头，表示飞机正飞向 VOR 台。另一个可选方位与之相差 180°。选定该方位时，箭头显示在“FROM”（背台）窗口，表示飞机正沿所选航向飞离 VOR。飞行员必须操纵飞机转到使 CDI 居中的航向，才能直接飞向或飞离 VOR。所显示的 VOR 信息来自对 VOR 地面台同时发射的两种信号相位关系的解算。当失去电源或 VOR 信号微弱、中断时，会出现 NAV 警告旗。

并不总是单独使用一个 VOR 信息指示表。随着飞行仪表和显示器的发展，VOR 导航信息已集成到其他仪表的显示中，例如无线电磁指示器（RMI）、水平状态指示器（HSI）、电子飞行仪表系统（EFIS）显示器或电子姿态指引仪（EADI）。飞行管理系统和自动飞行控制系统也被设计成集成 VOR 信息，以在计划的航段上自动控制飞机。平板多功能显示器（MFD）把 VOR 信息集成到移动地图显示和其他选定的显示中。不过，径向方位（以度表示）、航向偏差指示和向/背台信息这些基本内容始终未变。

在大型机场，仪表着陆系统（ILS）在仪表进近过程中引导飞机对准跑道。飞机的 VOR 接收机用来解译无线电信号，它在与 VOR 的 CDI 显示相同的仪表显示器上产生更灵敏的航向偏差指示。ILS 的这一部分称为航向信标，下文将予讨论。当调到 ILS 航向信标频率时，VOR/ILS 接收机的 VOR 电路不起作用。VOR 台常把 VOR 发射机与测距设备（DME）或诸如 ADF 发射机与天线之类的无方向信标（NDB）组合在一起。与 DME 配合使用时，飞行员可以借助 VOR 和 DME 精确确定自己的位置。由于 VOR 指示飞机相对 VOR 发射台的方位，而同址的 DME 指示到该台的距离，这就使飞行员不必飞越该台就能确知自己的位置。这些导航设备将在随后各节分别讨论。

VOR 设备的功能精度对飞行安全至关重要。VOR 接收机使用 VOR 测试设施（VOT）进行使用性测试。这些设施设于许多机场，可在相关地区的《机场设施目录》中查到。目录给出了在机场地面进行测试的具体地点。大多数 VOT 要求把 VOR 接收机调到 108.0 MHz 并使 CDI 居中。OBS 应指示 0° 且指示器显示 FROM，或指示 180° 且显示 TO。若用 RMI 作指示器，测试航向应始终指示 180°。有些维修站也能产生信号来测试 VOR 接收机，但不在 108.0 MHz 上。应联系该维修站获取发射频率并请其协助检查 VOR 系统。此项工作需在飞行日志中记录。

注：飞行员可利用 VOT 进行某些机上测试。用 VOT 测试 VOR 系统时，误差不应超过 ±4°。误差超过此值，在修复之前该飞机不得用于 IFR 飞行。装有两套 VOR 系统而仅共用天线的飞机，可通过比较两套系统的输出进行测试。把 VOR 接收机调到当地地面 VOR 台。方位指示相差不超过 ±4° 是允许的。

### 自动定向机（ADF）

自动定向机（ADF）依靠 NDB 发射的地面信号工作。早期的无线电定向机（RDF）使用同样的原理。当时用垂直极化天线发射 190 kHz 至 535 kHz 范围内的低频无线电波。飞机上的接收机调到 NDB 的发射频率。利用环形天线，通过监测所收信号的强度即可确定指向（或背向）该天线的方向。之所以可行，是因为无线电波从侧面作用于环形天线时会感应出零信号，而沿环面方向作用时感应的信号则强得多。NDB 信号用独特的莫尔斯电码脉冲调制，使飞行员能够识别其所导航的信标台。

使用 RDF 系统时，一个大型刚性环形天线安装在飞机机身内部，天线的正横方向垂直于飞机的纵轴。飞行员监听低频广播信号强度的变化，并操纵飞机保持零信号逐渐增强，从而飞向发射天线。飞越之后，随着飞机离台渐远，零信号逐渐减弱。零信号的增强或减弱是判断飞机飞向还是飞离 NDB 的唯一方法。偏离航向向左或向右会使信号强度因环形天线的接收特性而急剧增强。

ADF 在这一概念上作了改进。广播频率范围扩展到包括中频，最高约 1800 kHz。不再需要改变飞机航向来确定广播发射天线的方向。早期型号的 ADF 改用可旋转天线，天线转动以寻找信号为零的位置，广播天线的方向显示在驾驶舱内 ADF 指示器的方位刻度上。这种仪表至今仍在使用。它有一个固定刻度盘，0° 始终位于不转动的刻度盘顶部。指针指示到电台的相对方位。当指示为 0° 时，飞机正飞向（或飞离）该台。

随着 ADF 技术的进步，带可转方位刻度盘的指示器成为主流。收到 ADF 信号时，飞行员转动刻度盘使当前航向位于刻度顶部，这样指针就指示到 ADF 发射台的磁方位。这更直观，也与其他导航做法一致。

在现代 ADF 系统中，另有一副天线用来消除飞机是飞向还是飞离发射台的模糊性，称为辨向天线。辨向天线的接收场是全向的。它与环形天线的场组合后，形成一侧只有一个明显零接收区的场，用于调谐，并始终给出指向 ADF 台方向的指示。机载 ADF 接收机只需调到广播发射机的正确频率，系统即可工作。环形天线与辨向天线通常装在同一低剖面天线罩内。

任何在飞机接收机调谐能力范围内发射低频或中频无线电波的地面天线都可用来供 ADF 使用，其中包括调幅广播电台的天线。NDB 载波上加载可听识别音，通常采用两个字符的莫尔斯电码代号。接收调幅广播电台时，听到的是调幅广播节目而不是电台识别码。NDB 发射机的频率标在航图上该发射机符号旁边，识别代号也一并标出。

ADF 接收机可装在驾驶舱内，控制器便于使用者操作，许多通用航空飞机即如此。另一种方式是把 ADF 接收机装在远离驾驶舱的航空电子设备舱内，驾驶舱只留控制头。双套 ADF 接收机很常见。ADF 信息可显示在上述 ADF 指示器上，也可以是数字显示。现代平板多功能电子显示器通常以数字方式显示 ADF 信息。当在 ADF 接收机上选择 ANT 位时，环形天线被断开，只有辨向天线工作。这样可在 ADF 频率范围内更好地多方向接收广播，例如气象广播或 AWAS 广播。

当在 ADF 接收机/控制器上选择拍频振荡器（BFO）时，接收机内部的中频放大器接入一个内部拍频振荡器。这用于 NDB 不发射调制信号的情况。

ADF 技术的不断改进使其达到目前的状态。旋转接收天线已被带铁氧体磁芯的固定环形天线取代，从而提高了灵敏度，并可采用更小的天线。最现代的 ADF 系统装有两副互成 90° 的环形天线。所收信号感应出的电压送往分解器或测角器的两个定子。测角器定子在转子中感应出与固定环形天线信号相对应的电压。转子由电机驱动以寻找零位，同一电机带动驾驶舱指示器中的指针转动，显示到该台的相对方位或磁方位。

技术人员应注意，ADF 天线是指向性装置，其安装对指示正确与否至关重要。天线与机身纵轴或机头的校准很重要，零接收区必须出现在正确的方向上。天线的定向必须使飞机飞向该台时 ADF 指示台的位置，而不是背离时指示。应遵守制造商的所有说明。

### 无线电磁指示器（RMI）

为节省仪表板空间并把相关信息集中到便于使用的一处，研制了无线电磁指示器（RMI），它得到广泛应用。RMI 把磁罗盘、VOR 和 ADF 的指示合并在一个仪表中。

RMI 的方位刻度盘由远离仪表安装的磁通门罗盘驱动转动，因此始终指示飞机的磁航向。航向基准线通常是仪表盘顶部的一个标记或三角形。VOR 接收机驱动实心指针，指示飞向所调 VOR 台的磁方向。当 ADF 调到 NDB 时，双线（空心）指针指示到该 NDB 的磁方位。

由于磁通门罗盘不断调整方位刻度盘使飞机航向位于仪表顶部，飞行员的工作负荷得以减轻。指针指示 VOR 台和 ADF 台相对飞机当前位置的方向。按压按钮可使任一指针转换为 ADF 或 VOR，以适应使用两台同类型台站而无另一类台站的导航情况。

### 仪表着陆系统（ILS）

ILS 用于能见度差时使飞机着陆。这种无线电导航系统引导飞机沿下滑道下降到跑道接地区。ILS 使用多种无线电发射，从而实现精确的进近着陆。航向信标是其中一种无线电发射，用于提供对准跑道中心线的水平引导。单独的下滑道广播提供飞机沿正确下滑道下降到接地点的垂直引导。供外、中进近指点标使用的罗盘示位信标帮助飞行员切入进近导航设备系统。指点标提供距跑道距离的信息。所有这些无线电信号合在一起，使 ILS 成为非常精确可靠的飞机着陆手段。

#### 航向信标

航向信标广播是 VOR 频率低端（108 MHz–111.95 MHz）的甚高频广播，且仅用奇数频率。两个已调信号由设在进近跑道远端之外的水平极化天线阵产生。它们形成一个扩张的场，在距跑道 5 英里处宽 2 1/2°（约 1500 英尺），到着陆入口附近收窄至跑道宽度。进近区左侧充满以 90 Hz 信号调制的甚高频载波，右侧则含 150 MHz 调制信号。飞机的 VOR 接收机调到航向信标的甚高频频率，该频率可在公布的进近图和航图上查到。

当接收机使用航向信标电路时，标准 VOR 接收所特有的电路不起作用，而使用两者共用的部件。所收信号经滤波、整流为直流，用以驱动航向偏差指示器。若飞机收到 150 Hz 信号，VOR/ILS 显示器的 CDI 向左偏，表示跑道在左侧，飞行员必须向左转弯修正航向，从而使显示器上的 CDI 居中，并使飞机对准跑道中心线。若 VOR 接收机收到 90 Hz 信号，CDI 向右偏，飞行员必须向右转使 CDI 居中并使飞机对准跑道中心线。

#### 下滑道

ILS 的下滑道提供飞机着陆下降所需的垂直引导。下滑道提供正确下降角的垂直引导。无线电信号以约 3° 的角度把飞机引导到跑道接地点。下滑道发射天线位于进近跑道一侧，距跑道入口约 1000 英尺。它以楔形方向图发射，越接近跑道场越窄。

下滑道发射天线为水平极化。发射频率范围为 329.3 MHz 至 335.0 MHz 的特高频。该频率与 ILS 的航向信标频率配对。当 VOR/ILS 接收机调至该进近频率时，下滑道接收机自动调谐。与航向信标一样，下滑道发射两种信号，一种以 90 Hz 调制，另一种以 150 Hz 调制。飞机的下滑道接收机以类似航向信标接收机的方法解译信号，驱动一个称为下滑道指示器的垂直航向偏差指示器。下滑道指示器的工作方式与航向信标 CDI 完全相同，只是相差 90°。VOR/ILS 航向信标 CDI 与下滑道一起显示在飞机所装的任一种仪表上。

飞机接收下滑道信号所用的特高频天线有多种形式。常见的一种是把单个偶极天线装在机头内。天线制造商也已把下滑道接收功能并入用于接收 VHF VOR/ILS 航向信标的同一偶极天线。也使用刀形天线。[图 11-114] 图 11-115 所示为通用航空飞机 ILS 的 VOR 与下滑道接收机。

#### 罗盘示位信标

飞行员能够切入 ILS 才能使用它，这一点至关重要。罗盘示位信标就是为此目的而设置的发射机。通常有一座设在外指点标处，距跑道入口 4–7 英里；另一座可能设在中指点标处，距入口约 3500 英尺。外指点标罗盘示位信标是一台 25 瓦的 NDB，作用距离约 15 英里。它发射全向低频无线电波（190 Hz 至 535 Hz），用 ILS 识别码的前两个字母作键控。用 ADF 接收机切入该示位信标，因此无需额外设备。若设有中指点标罗盘示位信标，其情况类似，但用 ILS 识别码的后两个字母识别。定位之后，飞行员操纵飞机沿下滑道飞向跑道。

#### 指点标

指点标是 ILS 中最后使用的无线电发射机。它们发射信号，指示飞机沿下滑道到跑道的位置。如前所述，外指点标发射机设在距入口 4–7 英里处。它发射 75 MHz 载波，以 400 Hz 音频音调制，发成一串长划。该发射波束很窄，垂直向上。指点标接收机收到信号后，点亮仪表板上的一盏蓝灯。这一点，加上音频音，再配合航向信标和下滑道指示器，就能确定飞机在进近中的确切位置。

还使用中指点标。它设在进近中距跑道约 3500 英尺处，也以 75 MHz 发射。中指点标发射以 1300 Hz 音调制，发成一串点划，以免与外指点标全为长划的音混淆。收到该信号后，接收机点亮仪表板上的一盏琥珀色灯。

有些 ILS 进近设有内指点标，其发射信号以 3000 Hz 调制，只发一串点。它设在靠近跑道入口的着陆或复飞决断点。若设有内指点标，收到信号后点亮仪表板上的一盏白灯。三种指点标灯通常做在通用航空飞机的音频面板内，大型飞机上也可能单独设置。装电子显示的飞机通常把指点标灯或指示器设在姿态指引仪附近的下滑道显示旁。

ILS 无线电部件可用 ILS 测试装置测试。测试装置产生航向信标、下滑道和指点标信号，以确保接收机工作正常、驾驶舱仪表显示正确。

### 测距设备（DME）

许多 VOR 台与军用型 VOR 台（即 TACAN）设在同一地点，这时该导航台称为 VORTAC 台。民用飞机利用了 TACAN 的一项最初并未装在民用 VOR 台上的功能——DME。DME 系统计算飞机到 VORTAC 地面台 DME 设备的距离，并显示在驾驶舱内。当飞机飞向该台时，它还能显示计算出的飞机速度和到达所需时间。

后来，民用 VOR 台也设置了 DME 地面台，并且与 ILS 航向信标一起设置。这些分别称为 VOR/DME 和 ILS/DME 或 LOC/DME。后者在着陆时辅助进近跑道。DME 系统由机载 DME 收发机、显示器和天线，以及地面 DME 设备及其天线组成。

DME 之所以有用，是因为有了（来自 VOR 的）方位和到已知点（VOR 处的 DME 天线）的距离，飞行员就能确切确定飞机的位置。DME 工作在 962 MHz 至 1213 MHz 的特高频范围。自飞机正下方某点发射的载波信号，其传输路径较短。一些现代 DME 能够计算这一地面距离并显示出来。

### 区域导航（RNAV）

区域导航（RNAV）是一个通用术语，用来描述不直接飞越 VOR 台或 ADF 无方向信标等导航设备而从 A 点飞到 B 点的导航方式。它包括基于 VORTAC 和 VOR/DME 的系统，也包括基于 LORAN、GPS、INS 以及运输类飞机 FMS 的 RNAV 系统。不过，直到不久前，RNAV 一词最常用于描述利用本节所讨论的 VORTAC 和 VOR/DME 基准进行区域导航或从 A 点直飞 B 点的过程。

所有 RNAV 系统都使用航路点。航路点是用于定义航路或报告进度的指定地理位置或点。它可以用经纬度网格坐标定义或描述；对于基于 VOR 的 RNAV，则可描述为某条 VOR 径向线上的一个点再加上该点到 VOR 台的距离（例如 200/25 表示 VOR 台 200° 径向线上距台 25 海里的点）。

图 11-123 示出从 A 机场到 B 机场的一条 RNAV 飞行航路。图中所示的 VOR/DME 和 VORTAC 台用来建立“虚拟航路点”，飞机飞越的是这些虚拟航路点而不是实际的台。这样可以采用更直接的航路。虚拟航路点以“径向线/距离”数字对的形式输入 RNAV 航迹计算机（CLC）。计算机制造出这些航路点，并使飞机的 CDI 像对待实际 VOR 台那样工作。模式开关可在标准 VOR 导航与 RNAV 之间选择。

基于 VOR 的 RNAV 使用 VOR 接收机、天线和 VOR 显示设备（如 CDI）。RNAV 组件中的计算机用基本的几何和三角计算，给出每个航路点的航向、速度和时间读数。使用 RNAV 时，VOR 台必须在飞机的视距和有效作用范围内。

随着 GPS 的发展，RNAV 的灵活性不断提高。可以把 GPS 数据并入计划的 VOR RNAV 飞行计划，也可以完全不用任何 VOR 台而只用 GPS 规划航路。

### 雷达信标应答机

雷达信标应答机（简称应答机）在空管雷达屏幕上提供飞机的确切识别和位置。对于装有高度编码器的飞机，应答机还把飞机的气压高度提供出来，显示在代表该飞机的屏幕光点旁边。

机场的雷达能力各不相同。空管一般使用两类雷达。一次雷达按顺序向各个方向发射定向特高频或超高频无线电波。电波遇到飞机时，其中一部分反射回地面天线，接收机进行计算以确定飞机相对发射机的方向和距离。代表飞机的光点或目标显示在雷达屏幕上，该屏幕也称为平面位置显示器（PPI）。屏幕上给出方位角和按比例的距离，使管制员得到飞机的二维位置。空管还使用二次监视雷达（SSR）核实飞机位置，并为其位置增加高度这第三维。SSR 雷达发射编码脉冲串，由机上应答机接收。这些脉冲称为 3/A 模式脉冲，用于确认飞机的位置。与空管建立语音通信后，飞行员被指示在应答机上选择 4096 个离散编码之一，这些是八进制数字码。地面台以 1030 MHz 发射一个能量脉冲，应答机以 1090 MHz 发回附有所指配编码的应答。这通常通过改变雷达屏幕上的目标符号来确认飞机的位置。由于屏幕上可能布满许多已确认的飞机，空管还可要求飞行员“识别”（ident）。按下应答机上的 IDENT 按钮，应答机的发射方式使该机的目标符号在 PPI 上高亮显示，以便区分。

为获得高度信息，应答机控制必须置于 ALT 或 C 模式位。此时，响应脉冲询问发回空管的信号被加上一个编码，使飞机的气压高度显示在雷达屏幕目标符号旁边。应答机从与它电气相连的高度编码器获取飞机的气压高度。典型的飞机应答机天线如图 11-127 所示。

上述空管/飞机应答机系统称为空中交通管制雷达信标系统（ATCRBS）。为提高安全性，研制了 S 模式高度应答。采用 S 模式时，每架飞机预先分配一个唯一的识别码，当应答机响应 SSR 询问时，该识别码连同气压高度一起显示在空管雷达上。由于没有其他飞机用这个码应答，两名飞行员在应答机上选到同一应答码的可能性就被消除了。现代飞行数据处理计算机（FDP）指配信标码，并检索飞行计划数据中有用的信息，以数据块形式显示在屏幕上每架飞机的目标旁边。

S 模式有时称为“模式选择”。它是一种数据包协议，也用于机载防撞系统。空管使用 S 模式时，一次只询问一架飞机，应答机不必响应空域内的所有询问，从而减轻了工作负担。

此外，S 模式的位置信息更精确。只需一次应答，利用应答的相位计算位置（称为单脉冲），就足以确定飞机的位置。S 模式还具有交换更多种信息的能力，这是未来尚待开发的潜力。同时，它与较老的雷达和应答机技术保持了兼容性。

#### 应答机测试与检查

《联邦法规汇编》（CFR）第 14 编第 91 部第 91.413 节规定，飞入管制空域的飞机上的所有应答机，必须按照 14 CFR 第 43 部附录 F 每 24 个日历月检查测试一次。可能引入应答机误差的安装或维修，也须按附录 F 进行检查测试。只有相应等级的维修站、飞机制造商（若由其安装应答机）以及连续适航性大纲的持有者才被批准执行这些程序。与许多无线电电子设备一样，有测试设备可用来测试应答机的适航工作状态。

在机库或停机坪上操作应答机并不能使它免于被询问和应答。必须避免发射某些保留供紧急情况或军事活动使用的编码。地面操作时选择编码的程序是：把应答机置于 OFF 或 STANDBY 模式后再选择，以避免误发。0000 码保留供军用，是可发射的编码。7500 码用于劫机情况，7600 和 7700 码也保留供紧急使用。即使是误发保留给不在空管指挥下作目视飞行的 1200 码，也可能招致拦截行动。空管对从雷达信标应答机收到的所有信号都认真对待。

#### 高度编码器

高度编码器把飞机的气压高度转换成应答机发给空管的编码，通常以 100 英尺为增量报告。多年来编码器型式多样。有些做在仪表板所用高度表内部，用导线连到应答机。另一些装在航空电子设备架等看不见的地方，称为盲式编码器。在运输类飞机上，高度编码器可能是一个带静压管路接头、内部有膜盒的大黑盒子。现代通用航空编码器更小更轻，但仍常带内部膜盒和静压管路接头。有些编码器使用微晶体管，包括获取高度所用的压力敏感元件在内完全为固态，无需静压孔接头。与 GPS 及其他系统交换数据正变得普遍。

当应答机选择器置于 ALT 时，响应二次监视雷达询问所发出的数字脉冲信息就成为飞机气压高度的数字表示。共有 1280 个高度码，对应 1200 英尺平均海平面至 126700 英尺平均海平面之间每 100 英尺一个高度。每个高度增量分配一个编码。虽然这些编码是用于位置和 IDENT 的同一批编码中的 1280 个，但 C（或 S）模式询问会使 4096 个位置码失效，并使编码器起作用。正确的高度码送至应答机，由应答机响应询问。SSR 接收机将其识别为对 C（或 S）模式询问的应答，并把该码解译为高度码。

### 防撞系统

空中交通量的不断增长，使人们对防撞的关注相应增加。在今天日益拥挤的天空中，地面雷达、交通管制和目视警戒已不再够用。机载防撞设备长期以来是大型飞机的必备，如今在通用航空飞机上也已常见。

电子技术的新应用加上成本降低，使这一点成为可能。

#### 交通警戒与防撞系统（TCAS）

交通警戒与防撞系统（TCAS）是基于应答机的空对空交通监视与告警系统。TCAS 有两类。TCAS I 是为适应通用航空界和地区航空公司而研制的，该系统识别飞机 35–40 英里范围内的交通，并发出交通咨询（TA），帮助飞行员目视发现入侵飞机。10 至 30 座的飞机强制装用 TCAS I。

TCAS II 是更复杂的系统，国际上要求 30 座以上或重量超过 15 000 kg 的飞机装用。TCAS II 提供 TCAS I 的信息，还能分析接近飞机的预测航迹。如果即将发生碰撞或危险接近，TCAS II 计算机会发出决断咨询（RA），即给飞行员的口头指令，要求采取特定的规避动作（例如“下降”）。计算机的编程使入侵飞机（若也装有 TCAS II）的飞行员收到方向相反的规避动作 RA。

装有 TCAS 的飞机的应答机能够利用 SSR 技术（C 模式和 S 模式）询问附近其他飞机的应答机，使用的信号为 1030 MHz。被询问飞机的应答机以编码的 1090 MHz 信号应答，使 TCAS 计算机能够显示每架飞机的位置和高度。若飞机进入图 11-131 所示的水平或垂直距离之内，就发出可听 TA。飞行员必须决定是否采取措施以及采取什么措施。装有 TCAS II 的飞机利用连续的应答信息分析近距离目标飞机的速度和轨迹。如果算出即将碰撞，就发出 RA。

TCAS 目标飞机显示在驾驶舱的屏幕上，根据临近威胁等级用不同颜色和形状描绘接近的飞机。由于 RA 目前仅限于垂直规避动作，一些独立式 TCAS 显示器就是电子垂直速度指示器。多数飞机在导航屏幕或页面上用某种型式的电子 HSI 显示 TCAS 信息。多功能显示器可在同一屏幕上显示 TCAS 和气象雷达信息。TCAS 需要控制面板和计算机，与兼容的应答机及其天线配合工作，还需要与 EFIS 或其他先前安装或选定的显示器接口。

TCAS 也可称为机载防撞系统（ACAS），这是同一系统的国际名称。最新修订版的 TCAS II 称为第 7 版。这种 TCAS 信息的准确性和可靠性如此之高，以致要求飞行员执行 TCAS 的 RA 优先于空管的指令。

#### 广播式自动相关监视（ADS-B）

防撞是 FAA 改造国家空域系统（NAS）的 NextGen 计划的重要组成部分。在同样数量的空域和地面设施内容纳更多飞机，需要采用新技术来保持高水平的性能与安全。全球导航卫星系统（GNSS，如 GPS）的成功推广，促成了称为广播式自动相关监视（ADS-B）的防撞系统的研制。ADS-B 是 NextGen 计划的组成部分，其地面和机载基础设施正在建设之中。ADS-B 已在美国部分地区和世界各地投入使用。

ADS-B 分为两部分：ADS-B OUT 和 ADS-B IN。ADS-B OUT 把 GPS 接收机提供的定位信息与机上飞行状态信息（即包括高度、速度和时间在内的位置）结合起来，然后把这些信息广播给其他装有 ADS-B 的飞机和地面站。

这些广播用两种不同频率承载，具有数据链能力。第一种是扩大使用 1090 MHz 的 S 模式应答机协议，称为 1090 ES。第二种主要用于通用航空实施 ADS-B 的新型宽带方案，频率为 978 MHz，用 978 通用接入收发机（UAT）来实现。除 GPS 天线和接收机外，还需一副全向天线。ADS-B 的机载接收机利用这些信息，在类似 TCAS 的驾驶舱显示器上标出所发飞机的所在和移动情况。

与雷达相比，地面站造价低廉，因此可在偏远和被遮挡地区建设地面站以推广 ADS-B。地面站把来自机载 ADS-B 的信息与其他属于空中交通管理系统（ATMS）的地面站共享。数据传输无需人工确认，采用微波和卫星传输连接网络。

在交通间隔与管制方面，ADS-B 比常规地面雷达有几项优点。第一，可用低得多的费用覆盖整个空域。现有的老式空管雷达系统维护和更换费用高昂。此外，ADS-B 提供更精确的信息，因为矢量状态是飞机借助 GPS 卫星生成的。气象对 ADS-B 的影响大大减小，特高频 GPS 传输不受影响。定位精度提高，可实现更高密度的交通流量和进近着陆，这显然是在同样数量设施中起降更多飞机的必要条件。可获得更高程度的管制，还能选择航路以减少天气延误并获得最佳燃油消耗率。防撞范围扩大到包括机场地面上其他飞机和支持车辆的跑道侵入。

ADS-B IN 提供 TCAS 所没有的功能。装有该设备的飞机能接收大量数据以增强情景意识。交通信息服务广播（TIS-B）提供来自非 ADS-B 飞机和 ADS-B 飞机的交通信息（用不同频率）。地面雷达对地面目标的监视以及地面站链接网络中的任何交通数据，都通过 ADS-B IN 送到驾驶舱，从而提供比仅空对空防撞更完整的图像。ADS-B IN 还接收飞行信息服务广播（FIS-B）。具备 987 UAT 能力的飞机能够接收气象文字和图形、ATIS 信息和 NOTAM。

有 ADS-B 测试装置供经过培训的维修人员核实 ADS-B 设备工作是否正常。这一点至关重要，因为交通间隔的紧公差取决于每架飞机以及 ADS-B 系统所有部件提供的数据是否准确。

### 无线电高度表

无线电高度表（或雷达高度表）用于测量飞机到其正下方地形的距离，主要用于仪表进近以及 2500 英尺以下的低空或夜间飞行。无线电高度表为着陆决断高度提供主要高度信息。它带有可调的高度基准标记（bug），当飞机到达该高度时向飞行员发出目视或音响警告。通常，若到达决断高度仍看不到跑道，飞行员将中止着陆。

无线电高度表利用收发机和定向天线，从飞机上以 4.3 GHz 向地面直接发射载波。该波以 50 MHz 调频，以已知速度传播。它遇到地面特征后反射回飞机，由第二副天线接收回波信号。收发机通过测量信号往返经历的时间和发生的频率调制来处理该信号。显示器指示离地形的高度，也称为离地高度（AGL）。在低空获取 AGL 信息时，雷达高度表比气压高度表更精确、响应更快。收发机通常远离指示器安装。多功能和玻璃座舱显示器通常把雷达高度表的决断高度提示集成进来，以数字形式显示在屏幕上，并用基准标记、灯光或颜色变化指示飞机到达该高度。

大型飞机可将无线电高度表信息纳入近地警告系统（GPWS），该系统以音响提醒机组飞机下方地形可能存在的危险接近。图 11-141 中，决断高度（DH）窗口在 EADI 上显示雷达高度。

### 气象雷达

驾驶舱内常用的气象辅助设备有三类，常统称为气象雷达：

1. 机上实际雷达，用于探测和显示气象活动；

2. 闪电探测仪；以及 3. 由外部源上传到飞机的卫星或其他来源的气象雷达信息。

各种大小的飞机上都能见到机载气象雷达系统。其工作原理与空管一次雷达相似，只是无线电波是从降水而不是从飞机上反射回来。密集降水产生的回波比弱降水强。机载气象雷达接收机把强回波在驾驶舱显示器上显示为红色，中等回波为黄色，弱回波为绿色。云不产生回波。品红色保留用于显示强降水或极端降水或湍流。有些飞机有专用的气象雷达屏幕。多数现代飞机把气象雷达显示集成到导航显示器中。图 11-142 示出飞机上的气象雷达显示器。

气象雷达系统使用的无线电波处于超高频范围，例如 5.44 GHz 或 9.375 GHz。电波由通常位于非金属机头罩后的定向天线向飞机前方发射。发射的脉冲长度约 1 微秒。雷达收发机中的双工器在发射一个脉冲后把天线切换到接收状态约 2500 微秒，以接收和处理任何回波。这一循环反复进行，接收机电路据此建立起降水的二维图像供显示。增益调节控制雷达的作用距离。控制面板便于进行这一调节及其他调节。

严重湍流、风切变和冰雹是飞行员主要关心的问题。冰雹在气象雷达上会产生回波，而风切变和湍流则必须根据所探测到的任何降水的移动来判读。若装有此功能的气象雷达系统出现这种情况，会发出告警。干燥空气的湍流无法探测。当雷达扫描范围包含任何地形特征时，还必须抑制地物杂波。控制面板便于进行这一调节。

在气象雷达系统的维护和操作过程中，技术人员必须遵守特别的预防措施。覆盖天线的天线罩只能用经批准的涂料涂刷，以便无线电信号不受阻碍地通过。许多天线罩还装有接地条，把雷击和静电导离天线罩。

操作雷达时，重要的是遵守制造商的所有说明。所发射的高能辐射可能造成人身伤害，尤其是对眼睛和睾丸。不要正视正在发射的雷达天线。

除非使用特殊的电波吸收材料，否则不应在机库内操作雷达。此外，雷达指向建筑物时或正在进行加油时，也不应操作雷达。

雷达设备只能由……；闪电探测是识别潜在危险气象的第二种可靠手段。闪电会发出自己的电磁信号。雷击的方位可由使用环形天线的接收机算出，所用天线与 ADF 类似。有些闪电探测仪利用 ADF 天线。雷击的距离与其强度密切相关，强雷击被标示为靠近飞机。

Stormscope 是与闪电探测仪常联系在一起的一个专有名称，还有其他工作原理类似的设备。专用显示器在 200 英里范围内用小标记在屏幕上标出每次雷击的位置。随着时间推移，标记会变色以表示其“年龄”。无论如何，一小片区域内出现多次雷击就表明有一个雷暴单体，飞行员可以绕飞它。雷击也可标绘在多功能导航显示器上。

第三类气象雷达在各等级飞机上日益普遍。通过轨道卫星系统和/或地面上行链路（如 ADS-B IN 所述），气象信息几乎可以发到世界任何地方飞行中的飞机。这包括文字数据以及可叠加在飞机导航显示器上的实时雷达信息。远程生成并发送到飞机的气象雷达数据，通过对不同角度的各种雷达图像和卫星图像进行综合而得到提炼，从而更准确地描绘实际气象状况。综合地形数据库以消除地物杂波。补充数据包括国家气象局（NWS）和国家海洋与大气管理局（NOAA）可提供的全部信息。图 11-146 示出飞机收到的一份通俗语言气象摘要，以及通过卫星或地面链路气象信息服务可获得的其它气象信息一览。

如前所述，要接收 ADS-B 气象信号，机上须装有带相应天线的 1090 ES 或 970 UAT 收发机。卫星气象服务由与服务频率匹配的天线接收。接收机通常远离显示器安装，并与现有导航显示器和多功能显示器接口。手持 GPS 设备也可能具有卫星气象功能。

### 应急定位发射机（ELT）

应急定位发射机（ELT）是一种独立的电池供电发射机，由坠撞时经历的过大 G 力触发。它以 406.025 MHz 频率、5 瓦功率每隔 50 秒发射一次数字信号，至少持续 24 小时。该信号由科斯帕斯-萨萨特卫星系统中的卫星在世界任何地方接收。系统使用低地球轨道卫星（LEOSAT）和地球静止卫星（GEOSAT）两类卫星，能力不同而互补。信号在卫星上经过部分处理和存储，然后转发给称为本地用户终端（LUT）的地面站。信号在 LUT 进一步解译，并通过为此设立的任务控制中心（MCC）通知有关搜救机构。

注：海上船舶应急定位信标（EPIRB）和个人定位信标（PLB）使用完全相同的系统。科斯帕斯-萨萨特系统中美国部分由 NOAA 维护和运行。图 11-148 示出该系统的基本组成。

按 FAR 91.207 的规定，飞机上必须安装 ELT。这涵盖大多数不按第 135 部或第 121 部运行的通用航空飞机。ELT 必须在上次检查后 12 个月内检查安装是否正确、电池有无腐蚀、控制和坠撞传感器工作是否正常，以及天线处是否有足够的信号。机内自检设备便于在不发射应急信号的情况下进行测试。检查的其余部分为目视检查。告诫技术人员不要启动 ELT 而发出应急遇险信号。检查必须记入维修记录，包括电池新的到期日期。这一点也必须记录在案。ELT 通常尽可能安装在机身靠后、尾翼之前的位置。内装的 G 力传感器与飞机纵轴对齐。直升机的 ELT 可能装在机身的其他位置，它们装有可多方向触发的装置。所有 ELT 的正确安装、检查和维护，均应遵守 ELT 和机体制造商的说明。

图 11-149 示出 ELT 的安装位置。

利用多普勒技术，406 MHz ELT 信号源的位置可以计算到 2 至 5 公里以内。

第二代 406 MHz ELT 数字信号加载有来自 ELT 内部接收机或由外部设备集成进来的 GPS 位置坐标，这使坠撞地点的定位误差缩小到 100 米以内。

数字信号还加载有唯一的登记信息，可识别飞机、机主和联系信息等。收到信号时，用这些信息立即核查告警的真实性，以确保它是真正的应急发射，从而使救援资源……（原文此处中断）装在飞机上带自动 G 力触发的 ELT 易于拆卸，通常带可携带天线，使坠撞幸存者可以离开现场并随身携带正在工作的 ELT。驾驶舱内需装设面板，在 ELT 启动时提醒飞行员，并可在需要时使 ELT 预位、测试和人工启动。

现代 ELT 还可在 121.5 MHz 上发射信号。这是一种可用于归航的模拟发射。2009 年以前，121.5 MHz 是由科斯帕斯-萨萨特卫星监测的全球应急频率，但已被 406 MHz 标准取代。121.5 MHz 上的发射不再由卫星接收和转发。

FAA 并未强制要求使用 406 MHz ELT。较老的 121.5 MHz ELT 除新飞机外均满足 FAR 第 91.207 部的要求。数千架在美国注册的飞机仍装有启动时发射 0.75 瓦模拟 121.5 MHz 应急信号的 ELT。121.5 MHz 仍是应急频率，但不再由飞越的飞机和管制塔台监听。

要求技术人员在上次检查后 12 个月内对 121.5 MHz ELT 进行检查/测试，并按上述 406 MHz ELT 的同样完整性要求进行检查。然而，较老的 ELT 往往没有按 TSO C-126 认证的现代 ELT 那种机内自检电路，因此真正的使用性测试可能包括启动信号。可拆下天线并接上假负载来进行。任何 ELT 信号的启动都只允许在每小时整点至其后 5 分钟之间进行，启动持续时间不得超过三次可听扫频。建议测试前与当地管制塔台或飞行服务站联系。

必须注意，较老的 121.5 MHz 模拟信号 ELT 还常在 243.0 MHz 频率上发射应急信号。243.0 MHz 长期以来是军用应急频率，正逐步让位于数字 ELT 信号和卫星监测。121.5 MHz 发射机功能测试应按制造商说明进行。406 MHz ELT 在覆盖范围、定位精度、虚假告警识别和响应时间缩短方面的改进非常显著，目前已成为世界范围内的服务标准。

#### 406 MHz ELT 的测试注意事项

应注意防止意外触发搜救响应。ELT 意外启动会产生与真正紧急情况无法区分的应急信号，可能导致代价高昂且令人沮丧的搜索。此外，无正当理由的 ELT 信号可能占用应急频率，以致真正的应急信号无法被收到。还有，若 ELT 信号在机场内或附近发射，可能使某些无线电通信频道无法使用。

无论 ELT 位于何处、启动时间多长，406 MHz 信标的广播都会被科斯帕斯-萨萨特系统中至少一个地球静止本地用户终端（GEOLUT）探测到，也可能被每个低地球轨道本地用户终端（LEOLUT）探测到。告警信息将传送给该系统中每个任务控制中心（MCC）以便在世界范围内协调，并将作出响应（除非事先与科斯帕斯-萨萨特和地方当局进行了协调）。

首选直接连接测试，以防意外启动搜救响应系统。应尽可能避免向空中发射测试。最好使用天线罩套，或把测试设备直接接到天线端口。在金属机库内测试 ELT 系统，并不能保证所辐射的信号不会被科斯帕斯-萨萨特系统探测到。在机库内测试 ELT 设备的技术人员，应把该测试当作在室外测试来对待。

测试 ELT 时，应使用 50 欧姆假负载或天线罩套，以防信号辐射到空间。信号必须衰减到低于 -51 dBW（功率通量密度为 -37.4 dB (W/m2)，或场强为 -11.6 dB (V/m)）。

若必须进行空中发射测试，技术人员应仔细遵守科斯帕斯-萨萨特的说明，并使用 ELT 设备上的机内测试信息。ELT 测试信息与紧急情况下发射的信息不同，但仍能被科斯帕斯-萨萨特系统探测到。进行空中发射测试前应先联系科斯帕斯-萨萨特，联系网址为 www.cospas-sarsat.int/en/。若必须进行空中发射测试，还应事先联系当地空管部门。

遵照测试装置说明，或把测试装置放在距 ELT 天线至少 12 米（39.4 英尺）处。对 ELT 发射的每个模式和频率进行测试。

#### 406 MHz 测试

核实设备输出信号不小于 17 dBm（50 mW），且不大于 26 dBm（400 mW）。

核实设备在正确频率上发射。可通过运行 ELT 自检并用 ELT 测试装置检测信号来完成。收到并解出测试信息，说明设备在正确频率上发射。

使用合适的测试设备和屏蔽，记录 ELT 所发射的编码，并核实该 ELT 编码已在科斯帕斯-萨萨特登记。测试技术人员或机主应核实科斯帕斯-萨萨特档案中的信息准确且为最新。

确认在发动机关闭时驾驶舱内能听到 ELT 的音响指示，且从机组正常坐姿能看见目视指示。如有可能，应以不会引起搜救响应的方式进行（例如装上假负载）。

对 G 开关进行使用性检查。应以不会引起搜救响应的方式进行（例如装上假负载）。若 G 开关不能触发，应予更换。

确保除 406 MHz 发射机输出端外的所有电缆重新接好。如有可能，确保 406 MHz 发射机接到测试装置上。启动 ELT（若装有遥控开关则使用遥控开关），判断系统是否辐射强的 406 MHz 信号。必要时确保系统复位。

若装有水激活电路，如有可能把 ELT 接到测试装置上。短接水传感引线启动 ELT，判断系统是否辐射强的 406 MHz 信号。必要时确保系统复位。

### 远程导航系统（LORAN）

远程导航系统（LORAN）是一种已在美国停止使用的 RNAV。它研制于第二次世界大战期间，最新的 LORAN-C 型对飞行员和航海人员都非常有用而精确。LORAN 利用一系列发射塔发出的无线电波脉冲和机载接收机/计算机，在发射塔网络中确切确定飞机的位置。北美共建有十二条 LORAN 发射塔“链”。每条链有一座主发射塔和若干副塔。所有发射机的广播都在同一频率 100 kHz 上，因此 LORAN 接收机无需调谐。由于处于低频范围，LORAN 的发射传播距离远，用少量台站即可提供良好覆盖。

链中各塔发射时间精确同步的脉冲信号。LORAN 接收机测量收到主塔和链中另外两座塔脉冲的时间，根据代表来自各已知点的信号传播时间的抛物线的交点，算出飞机的位置。

GPS 导航的精度和普及，使美国政府以冗余和运行发射塔费用高昂为由停止了对 LORAN 导航系统的支持。尚未改装的飞机上的面板式 LORAN 导航组件很可能被拆下，换装 GPS 组件。

### 全球定位系统（GPS）

全球定位系统（GPS）导航是航空中发展最快的导航方式。它利用美国政府设置并维护在地球轨道上的 NAVSTAR 卫星群来实现。卫星连续发射编码信号，使装有 GPS 接收机的飞机能极精确地定位。GPS 可单独用于航路导航，也可集成到其他导航系统中，如 VOR/RNAV、惯性基准系统或飞行管理系统。

GPS 分为三个部分：空间部分、控制部分和用户部分。飞机技术人员只涉及用户部分的设备，如 GPS 接收机、显示器和天线。

24 颗卫星（21 颗工作、3 颗备份）分布在 6 个独立轨道面内，高度 12625 英里，构成 GPS 系统的空间部分。卫星的布置使地球上任何地点在任一时刻至少有 4 颗卫星处于地平线以上至少 15°。通常可见 5 至 8 颗卫星。每颗卫星发射两种载有数字编码信息的信号。民用航空使用 1575.42 MHz 载频上的 L1 频道发射。卫星识别、位置和时间连同状态及其他信息，通过这一数字调制信号传给飞机 GPS 接收机。L2 频道 1227.60 MHz 发射供军用。

信号从发射卫星到达飞机 GPS 接收机所需的时间，与每颗卫星的精确位置相结合，用以算出飞机的位置。GPS 的控制部分监测每颗卫星，确保其位置和时间精确。这一控制由五个地面接收站、一个主控站和三副发射天线完成。接收站把从卫星收到的状态信息转给主控站，经计算后通过发射机向卫星发送修正指令。

GPS 的用户部分由装在飞机上的数千台接收机以及所有其他使用 GPS 发射信号的接收机组成。具体对飞机技术人员而言，用户部分包括控制面板/显示器、GPS 接收机电路和天线。控制、显示和接收部分通常装在一个组件内，该组件还可能包括 VOR/ILS 电路和甚高频通信收发机。玻璃座舱飞机的多功能显示器集成了 GPS 信息。

GPS 接收机测量信号从三颗发射卫星到达所需的时间。由于无线电波以每秒 186000 英里的速度传播，到每颗卫星的距离可以算出。这些距离的交点给出飞机的二维位置，以经纬度坐标表示。再加入与第四颗卫星的距离，还可算出离地球表面的高度，从而得到三维定位。增加更多卫星输入可提高定位精度。

解算出飞机位置后，GPS 组件处理许多有用的导航输出，如速度、方向、到航路点的方位、已飞距离、到达时间等，可选择显示使用。航路点可输入并存储在组件存储器中。地形特征、机场数据、VOR/RNAV 和进近信息、通信频率等也可装入 GPS 组件。多数现代组件具有移动地图显示能力。

使用 GPS 的一个主要优点是不受天气造成服务中断的影响。载波穿过电离层时会引入误差，但这些误差得到修正并保持在最低限度。GPS 也相对便宜。用于飞机 IFR 导航的 GPS 接收机必须按 TSO-129A 制造，这使其价格高于徒步或汽车用的手持设备。但由于基础设施规模小，GPS 的总成本较低。大部分固有精度做在空间和控制部分中，因而用便宜的用户设备即可可靠定位。

目前 GPS 的精度为水平 20 米以内，垂直略差。这对航路导航已足够，且精度高于要求。但离场和进近要求更严格的精度。集成广域增强系统（WAAS）可把 GPS 精度提高到 7.6 米以内，下文将予讨论。GPS 的未来要求通过每颗卫星增加两种新发射来提高精度：L2C 频道用于非安全关键的普通应用；航空专用的 L5 频道提供 I、II、III 类着陆所需的精度，并与 ADS-B 一起支撑 NextGen 国家空域系统计划。

#### 广域增强系统（WAAS）

为提高 GPS 用于飞机导航的精度，研制了广域增强系统（WAAS）。它由约 25 个经过精确测量的地面站组成，这些站接收 GPS 信号，最终向飞机发送修正信息。WAAS 各组成部分及其工作情况见图 11-154。

WAAS 地面站接收 GPS 信号，把位置误差转给两个主地面站。经分析时间和位置信息后，把修正指令发给位于国家空域系统上方地球静止轨道上的通信卫星。卫星广播类似 GPS 的信号，具有 WAAS 功能的 GPS 接收机用这些信号修正从 GPS 卫星收到的位置信息。

使用广域增强系统需要具有 WAAS 功能的 GPS 接收机。若装有该设备，飞机即有资格在没有任何地面进近设备的情况下对数千个机场实施精密进近。装有 WAAS 的飞机之间的间隔最低标准也可降低。已知 WAAS 系统可把位置误差降到水平和垂直方向 1–3 米。

## 3. 专业词汇

| 英文 | 词性 | 中文 | 本节语境 |
| --- | --- | --- | --- |
| very high frequency omni-directional range (VOR) | n. | 甚高频全向信标 | 陆基发射台，信号向 360° 传播，机载接收机据以确定方位 |
| course deviation indicator (CDI) | n. | 航向偏差指示器 | 以中央刻度的左右偏移显示飞机偏离所选航道的指示器 |
| omni-bearing selector (OBS) | n. | 全向方位选择器 | 转动方位环选定航道、使 CDI 居中的旋钮 |
| radial | n. | 径向线 | 以 VOR 台为起点的磁方位线，RNAV 用径向线加距离定义航路点 |
| localizer | n. | 航向信标 | ILS 中提供对准跑道中心线水平引导的甚高频发射 |
| glideslope | n. | 下滑道 | ILS 中提供约 3° 下降角垂直引导的特高频发射 |
| marker beacon | n. | 指点标 | 进近航路上垂直向上发射窄波束、用灯光与音调报距的台站 |
| transponder | n. | 应答机 | 接收地面二次雷达询问并回发编码和气压高度的机载设备 |
| altitude encoder | n. | 高度编码器 | 把气压高度转换成每 100 英尺一档的数字码送给应答机 |
| resolution advisory (RA) | n. | 决断咨询 | TCAS II 判断碰撞即将发生时给出的具体规避口令 |
| traffic advisory (TA) | n. | 交通咨询 | TCAS 提示附近有飞机、帮助飞行员目视发现的告警 |
| ground clutter | n. | 地物杂波 | 气象雷达波照射地形产生的无用回波，须予以抑制 |
| dummy load | n. | 假负载 | 测试 ELT 时接在天线端吸收射频、防止信号外泄的负载 |
| waypoint | n. | 航路点 | RNAV/GPS 中用于定义航路或报告进度的地理位置 |

## 4. 语法解析

### ① 主系表结构加冒号列举（“四个主要部件是……”）
**原句**：The four main components of a typical system are: a receiver, a visual indicator, a frequency selector (controller or control panel), and antennas.
**拆解**：主干为“The four main components … are”，系动词 are 后接冒号引出的四个并列名词短语作表语；of a typical system 为介词短语后置修饰主语 components；括号内 controller or control panel 是对 frequency selector 的同位解释。
**要点**：冒号后的列举与主语 components 构成“主—表”对应，汉语宜译成“四个主要部件是：……”；括号内的同义解释不是第五个部件，数词 four 必须与列举项数一致。

### ② 被动语态加 since 原因状语从句
**原句**：A pilot is not required to fly a pattern to intersect the signal from a VOR station since it propagates out in every direction.
**拆解**：主句为被动结构“A pilot is not required to fly a pattern”，不定式 to intersect the signal from a VOR station 作 fly a pattern 的目的状语；since 引导原因状语从句，it 指代前面的 the signal。
**要点**：is not required to 宜译“不要求……”，比“飞行员不被要求”自然；since 在此表原因而非时间，不能译成“自从”；从句主语 it 翻译时应还原为“信号”。

### ③ 并列谓语加多层介词短语作定语
**原句**：The receiver in the aircraft deciphers the phase difference and determines the aircraft’s position in degrees from the VOR ground based unit.
**拆解**：主语 The receiver 后接 in the aircraft 作后置定语；谓语由 deciphers 与 determines 两个动词并列构成；in degrees 和 from the VOR ground based unit 两个介词短语都修饰 position，分别表示“以度为单位”和“相对该地面台”。
**要点**：两个介词短语都挂在 position 上，而不是修饰 determines，否则会误读成“从台站确定”；汉语习惯把 in degrees 提前，译作“以度表示的方位”。

### ④ when 引导的省略式状语从句加 until 时间状语从句
**原句**：When in range of a VOR, the pilot rotates the OBS until the course deviation indicator centers.
**拆解**：When in range of a VOR 是省略了主语和系动词的时间状语从句，完整形式为 When the aircraft is in range of a VOR；主句为 the pilot rotates the OBS；until 引导时间状语从句，centers 在此为不及物动词，意为“居中”。
**要点**：状语从句省略主语时须与主句主语一致，这里省略的是 the aircraft 而不是 the pilot，翻译要补出“飞机处于覆盖范围内”；until 表示动作持续到某状态出现，译“直到……居中为止”。

### ⑤ 并列主语加被动语态加插入语
**原句**：Only an appropriately rated repair station, the aircraft manufacturer (if it installed transponder), and holders of a continuous airworthy program are approved to conduct the procedures.
**拆解**：主语为三个并列名词短语——repair station、the aircraft manufacturer、holders of a continuous airworthy program，Only 限定主语范围；括号内 if it installed transponder 是插入的条件从句，说明制造商的适用情形；谓语为被动结构 are approved to conduct the procedures。
**要点**：三个并列项共同作 are approved 的主语，故谓语用复数 are；Only 要体现在“只有……才被批准”上；插入语宜单独处理，不要打断并列关系。

### ⑥ since 原因从句加主系表
**原句**：Since RAs are currently limited to vertical evasive maneuvers, some stand-alone TCAS displays are electronic vertical speed indicators.
**拆解**：Since 引导原因状语从句，从句为被动结构 are limited to …；主句为主系表 some stand-alone TCAS displays are electronic vertical speed indicators，主语带 stand-alone 作前置定语。
**要点**：be limited to 意为“仅限于”，不是“被限制住”；因 RA 只含垂直机动，独立显示器才做成垂直速度表，这条因果链是理解全句的关键。
