from scimma.client import stream

test_data = {
    'GCN': [{'title': 'GCN CIRCULAR',
             'number': 27466,
             'subject': 'GRB 200327A: Fermi GBM detection',
             'publisher': 'Peter Veres',
             'content': '''At 20:56:48.17 UT on 27 March 2020, the Fermi Gamma-Ray Burst Monitor (GBM) triggered
                           and located GRB 200327A (trigger 607035413 / 200327873) which was also
                           detected by AGILE-MCAL (Ursi et al., GCN 27461) and localized by IPN (Svinkin
                           et al., GCN 27463). The GBM on-ground location is consistent with the IPN
                           position.'''},
            {'title': 'GCN CIRCULAR',
             'number': 27485,
             'subject': 'LIGO/Virgo S200225q: Upper limits from Konus-Wind observations',
             'publisher': 'Anna Ridnaia',
             'content': '''Konus-Wind (KW) was observing the whole sky at the time of the
                           LIGO/Virgo event S200225q (2020-02-25 06:04:21.397 UTC, hereafter T0;
                           LIGO/Virgo Collaboration GCN Circ. 27193).'''},
            {'title': 'GCN CIRCULAR',
             'number': 27445,
             'subject': 'GRB 200324A: AROMA-N Optical Observation',
             'publisher': 'Takanori Sakamoto',
             'content': '''22 images of 60 sec, 120 sec, 180 sec and 300 sec exposures
                           were taken in the R filter starting from March 24 16:42:55 (UT)
                           about 228 seconds after the trigger and stopped on March 24 19:06:11 (UT).
                           We do not detect the optical afterglow both in the individual
                           images and the stacked image.  The estimated five sigma upper limit
                           of the combined image (total exposure of 3240 sec) is ~17.6 mag
                           using the USNO-B1 catalog.'''},
            {'title': 'GCN CIRCULAR',
             'number': 27403,
             'subject': 'LIGO/Virgo S200316bj: No counterpart candidates in Fermi-LAT observations',
             'publisher': 'Milena Crnogorcevic',
             'content': '''We performed a search for a transient counterpart within the observed region of 
                           the 90% contour of LIGO map in a fixed time window from T0 to T0 + 10 ks. 
                           No significant new sources are found.'''},
            {'title': 'GCN CIRCULAR',
             'number': 27333,
             'subject': 'GRB 200306C: SAO RAS observations of OT',
             'publisher': 'Moskvitin Alexander',
             'content': '''We clearly detected the OT discovered by Swift/UVOT, MASTER-Net
                           (Lipunov et al. GCNC #27324/27325/27327), FRAM-ORM (Jelinek et al.
                           GCNC #27328), BOOTES-1 (Hu et al., GCNC #27329) with the coordinates:
                           R. A. = 13:14:13.44, Decl. = +11:16:11.8 +/- 0".5, Epoch = 2000.0.'''}],
    'ATEL': [{'title': 'C/2019 Y4 ATLAS',
              'number': 13622,
              'subject': 'confirmation of nuclear change',
              'publisher': 'Iain Steele',
              'content': '''We confirm the appearance of a nuclear elongation reported by Ye & Zhang, 
                            with a total nuclear elongation of 3.5 arcserc at the time of our second 
                            epoch of observations. The distribution of nuclear material appears somewhat 
                            bimodal, with a suggested gap between a sharper "leading" peak and a 
                            following more extended section.'''},
             {'title': 'Fermi-LAT detection of renewed gamma-ray activity',
              'number': 13558,
              'subject': 'FSRQs PKS 0208-512 and 4C +50.11',
              'publisher': 'Roberto Angioni',
              'content': '''The Large Area Telescope (LAT), one of the two instruments on the Fermi 
                            Gamma-ray Space Telescope, has observed renewed gamma-ray flaring activity 
                            from two sources positionally consistent with the flat-spectrum radio 
                            quasar PKS 0208-512, also known as 4FGL J0210.7-5101'''},
             {'title': 'Swift-BAT detection of bursts',
              'number': 13572,
              'subject': 'XTE J1701-407',
              'publisher': 'David M. Palmer',
              'content': '''At 23:45:29 UTC on 2020-03-18, BAT detected a burst from the source XTE 
                            J1701-407, which has recently been reported as in outburst (ATel #13564, 
                            Onori et al.). The burst is roughly 40 seconds long and reaches a peak of 
                            ~400 counts/s (15-50 keV).'''}]
    }


for topic, messages in test_data.items():
    with stream.open(f'kafka://localhost:9092/{topic}', 'w', format='json') as s:
        for message in messages:
            s.write(message)
