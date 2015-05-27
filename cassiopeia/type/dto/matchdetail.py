from cassiopeia.type.dto.common import CassiopeiaDto


class MatchDetail(CassiopeiaDto):
    def __init__(self, dictionary):
        # int # Match map ID
        self.mapId = dictionary["mapId"]

        # long # Match creation time. Designates when the team select lobby is created and/or the match is made through match making, not when the game actually starts.
        self.matchCreation = dictionary["matchCreation"]

        # long # Match duration
        self.matchDuration = dictionary["matchDuration"]

        # long # ID of the match
        self.matchId = dictionary["matchId"]

        # string # Match mode (Legal values: CLASSIC, ODIN, ARAM, TUTORIAL, ONEFORALL, ASCENSION, FIRSTBLOOD, KINGPORO)
        self.matchMode = dictionary["matchMode"]

        # string # Match type (Legal values: CUSTOM_GAME, MATCHED_GAME, TUTORIAL_GAME)
        self.matchType = dictionary["matchType"]

        # string # Match version
        self.matchVersion = dictionary["matchVersion"]

        # list<ParticipantIdentity> # Participant identity information
        self.participantIdentities = [ParticipantIdentity(pi) if not isinstance(pi,ParticipantIdentity) else pi for pi in dictionary["participantIdentities"]]

        # list<Participant> # Participant information
        self.participants = [Participant(p) if not isinstance(p,Participant) else p for p in dictionary["participants"]]

        # string # Platform ID of the match
        self.platformId = dictionary["platformId"]

        # string # Match queue type (Legal values: CUSTOM, NORMAL_5x5_BLIND, RANKED_SOLO_5x5, RANKED_PREMADE_5x5, BOT_5x5, NORMAL_3x3, RANKED_PREMADE_3x3, NORMAL_5x5_DRAFT, ODIN_5x5_BLIND, ODIN_5x5_DRAFT, BOT_ODIN_5x5, BOT_5x5_INTRO, BOT_5x5_BEGINNER, BOT_5x5_INTERMEDIATE, RANKED_TEAM_3x3, RANKED_TEAM_5x5, BOT_TT_3x3, GROUP_FINDER_5x5, ARAM_5x5, ONEFORALL_5x5, FIRSTBLOOD_1x1, FIRSTBLOOD_2x2, SR_6x6, URF_5x5, ONEFORALL_MIRRORMODE_5x5, BOT_URF_5x5, NIGHTMARE_BOT_5x5_RANK1, NIGHTMARE_BOT_5x5_RANK2, NIGHTMARE_BOT_5x5_RANK5, ASCENSION_5x5, HEXAKILL, KING_PORO_5x5, COUNTER_PICK)
        self.queueType = dictionary["queueType"]

        # string # Region where the match was played
        self.region = dictionary["region"]

        # string # Season match was played (Legal values: PRESEASON3, SEASON3, PRESEASON2014, SEASON2014, PRESEASON2015, SEASON2015)
        self.season = dictionary["season"]

        # list<Team> # Team information
        self.teams = [Team(t) if not isinstance(t,Team) else t for t in dictionary["teams"]]

        # Timeline # Match timeline data (not included by default)
        self.timeline = Timeline(dictionary["timeline"]) if not isinstance(dictionary["timeline"],Timeline) else dictionary["timeline"]



class Participant(CassiopeiaDto):
    def __init__(self, dictionary):
        # int # Champion ID
        self.championId = dictionary["championId"]

        # string # Highest ranked tier achieved for the previous season, if any, otherwise null. Used to display border in game loading screen. (Legal values: CHALLENGER, MASTER, DIAMOND, PLATINUM, GOLD, SILVER, BRONZE, UNRANKED)
        self.highestAchievedSeasonTier = dictionary["highestAchievedSeasonTier"]

        # list<Mastery> # List of mastery information
        self.masteries = [Mastery(m) if not isinstance(m,Mastery) else m for m in dictionary["masteries"]]

        # int # Participant ID
        self.participantId = dictionary["participantId"]

        # list<Rune> # List of rune information
        self.runes = [Rune(r) if not isinstance(r,Rune) else r for r in dictionary["runes"]]

        # int # First summoner spell ID
        self.spell1Id = dictionary["spell1Id"]

        # int # Second summoner spell ID
        self.spell2Id = dictionary["spell2Id"]

        # ParticipantStats # Participant statistics
        self.stats = ParticipantStats(dictionary["stats"]) if not isinstance(dictionary["stats"],ParticipantStats) else dictionary["stats"]

        # int # Team ID
        self.teamId = dictionary["teamId"]

        # ParticipantTimeline # Timeline data. Delta fields refer to values for the specified period (e.g., the gold per minute over the first 10 minutes of the game versus the second 20 minutes of the game. Diffs fields refer to the deltas versus the calculated lane opponent(s).
        self.timeline = ParticipantTimeline(dictionary["timeline"]) if not isinstance(dictionary["timeline"],ParticipantTimeline) else dictionary["timeline"]



class ParticipantIdentity(CassiopeiaDto):
    def __init__(self, dictionary):
        # int # Participant ID
        self.participantId = dictionary["participantId"]

        # Player # Player information
        self.player = Player(dictionary["player"]) if not isinstance(dictionary["player"],Player) else dictionary["player"]



class Team(CassiopeiaDto):
    def __init__(self, dictionary):
        # list<BannedChampion> # If game was draft mode, contains banned champion data, otherwise null
        self.bans = [BannedChampion(c) if not isinstance(c,BannedChampion) else c for c in dictionary["bans"]]

        # int # Number of times the team killed baron
        self.baronKills = dictionary["baronKills"]

        # long # If game was a dominion game, specifies the points the team had at game end, otherwise null
        self.dominionVictoryScore = dictionary["dominionVictoryScore"]

        # int # Number of times the team killed dragon
        self.dragonKills = dictionary["dragonKills"]

        # boolean # Flag indicating whether or not the team got the first baron kill
        self.firstBaron = dictionary["firstBaron"]

        # boolean # Flag indicating whether or not the team got first blood
        self.firstBlood = dictionary["firstBlood"]

        # boolean # Flag indicating whether or not the team got the first dragon kill
        self.firstDragon = dictionary["firstDragon"]

        # boolean # Flag indicating whether or not the team destroyed the first inhibitor
        self.firstInhibitor = dictionary["firstInhibitor"]

        # boolean # Flag indicating whether or not the team destroyed the first tower
        self.firstTower = dictionary["firstTower"]

        # int # Number of inhibitors the team destroyed
        self.inhibitorKills = dictionary["inhibitorKills"]

        # int # Team ID
        self.teamId = dictionary["teamId"]

        # int # Number of towers the team destroyed
        self.towerKills = dictionary["towerKills"]

        # int # Number of times the team killed vilemaw
        self.vilemawKills = dictionary["vilemawKills"]

        # boolean # Flag indicating whether or not the team won
        self.winner = dictionary["winner"]



class Timeline(CassiopeiaDto):
    def __init__(self, dictionary):
        # long # Time between each returned frame in milliseconds.
        self.frameInterval = dictionary["frameInterval"]

        # list<Frame> # List of timeline frames for the game.
        self.frames = [Frame(f) if not isinstance(f,Frame) else f for f in dictionary["frames"]]



class Mastery(CassiopeiaDto):
    def __init__(self, dictionary):
        # long # Mastery ID
        self.masteryId = dictionary["masteryId"]

        # long # Mastery rank
        self.rank = dictionary["rank"]



class ParticipantStats(CassiopeiaDto):
    def __init__(self, dictionary):
        # long # Number of assists
        self.assists = dictionary["assists"]

        # long # Champion level achieved
        self.champLevel = dictionary["champLevel"]

        # long # If game was a dominion game, player's combat score, otherwise 0
        self.combatPlayerScore = dictionary["combatPlayerScore"]

        # long # Number of deaths
        self.deaths = dictionary["deaths"]

        # long # Number of double kills
        self.doubleKills = dictionary["doubleKills"]

        # boolean # Flag indicating if participant got an assist on first blood
        self.firstBloodAssist = dictionary["firstBloodAssist"]

        # boolean # Flag indicating if participant got first blood
        self.firstBloodKill = dictionary["firstBloodKill"]

        # boolean # Flag indicating if participant got an assist on the first inhibitor
        self.firstInhibitorAssist = dictionary["firstInhibitorAssist"]

        # boolean # Flag indicating if participant destroyed the first inhibitor
        self.firstInhibitorKill = dictionary["firstInhibitorKill"]

        # boolean # Flag indicating if participant got an assist on the first tower
        self.firstTowerAssist = dictionary["firstTowerAssist"]

        # boolean # Flag indicating if participant destroyed the first tower
        self.firstTowerKill = dictionary["firstTowerKill"]

        # long # Gold earned
        self.goldEarned = dictionary["goldEarned"]

        # long # Gold spent
        self.goldSpent = dictionary["goldSpent"]

        # long # Number of inhibitor kills
        self.inhibitorKills = dictionary["inhibitorKills"]

        # long # First item ID
        self.item0 = dictionary["item0"]

        # long # Second item ID
        self.item1 = dictionary["item1"]

        # long # Third item ID
        self.item2 = dictionary["item2"]

        # long # Fourth item ID
        self.item3 = dictionary["item3"]

        # long # Fifth item ID
        self.item4 = dictionary["item4"]

        # long # Sixth item ID
        self.item5 = dictionary["item5"]

        # long # Seventh item ID
        self.item6 = dictionary["item6"]

        # long # Number of killing sprees
        self.killingSprees = dictionary["killingSprees"]

        # long # Number of kills
        self.kills = dictionary["kills"]

        # long # Largest critical strike
        self.largestCriticalStrike = dictionary["largestCriticalStrike"]

        # long # Largest killing spree
        self.largestKillingSpree = dictionary["largestKillingSpree"]

        # long # Largest multi kill
        self.largestMultiKill = dictionary["largestMultiKill"]

        # long # Magical damage dealt
        self.magicDamageDealt = dictionary["magicDamageDealt"]

        # long # Magical damage dealt to champions
        self.magicDamageDealtToChampions = dictionary["magicDamageDealtToChampions"]

        # long # Magic damage taken
        self.magicDamageTaken = dictionary["magicDamageTaken"]

        # long # Minions killed
        self.minionsKilled = dictionary["minionsKilled"]

        # long # Neutral minions killed
        self.neutralMinionsKilled = dictionary["neutralMinionsKilled"]

        # long # Neutral jungle minions killed in the enemy team's jungle
        self.neutralMinionsKilledEnemyJungle = dictionary["neutralMinionsKilledEnemyJungle"]

        # long # Neutral jungle minions killed in your team's jungle
        self.neutralMinionsKilledTeamJungle = dictionary["neutralMinionsKilledTeamJungle"]

        # long # If game was a dominion game, number of node captures
        self.nodeCapture = dictionary["nodeCapture"]

        # long # If game was a dominion game, number of node capture assists
        self.nodeCaptureAssist = dictionary["nodeCaptureAssist"]

        # long # If game was a dominion game, number of node neutralizations
        self.nodeNeutralize = dictionary["nodeNeutralize"]

        # long # If game was a dominion game, number of node neutralization assists
        self.nodeNeutralizeAssist = dictionary["nodeNeutralizeAssist"]

        # long # If game was a dominion game, player's objectives score, otherwise 0
        self.objectivePlayerScore = dictionary["objectivePlayerScore"]

        # long # Number of penta kills
        self.pentaKills = dictionary["pentaKills"]

        # long # Physical damage dealt
        self.physicalDamageDealt = dictionary["physicalDamageDealt"]

        # long # Physical damage dealt to champions
        self.physicalDamageDealtToChampions = dictionary["physicalDamageDealtToChampions"]

        # long # Physical damage taken
        self.physicalDamageTaken = dictionary["physicalDamageTaken"]

        # long # Number of quadra kills
        self.quadraKills = dictionary["quadraKills"]

        # long # Sight wards purchased
        self.sightWardsBoughtInGame = dictionary["sightWardsBoughtInGame"]

        # long # If game was a dominion game, number of completed team objectives (i.e., quests)
        self.teamObjective = dictionary["teamObjective"]

        # long # Total damage dealt
        self.totalDamageDealt = dictionary["totalDamageDealt"]

        # long # Total damage dealt to champions
        self.totalDamageDealtToChampions = dictionary["totalDamageDealtToChampions"]

        # long # Total damage taken
        self.totalDamageTaken = dictionary["totalDamageTaken"]

        # long # Total heal amount
        self.totalHeal = dictionary["totalHeal"]

        # long # If game was a dominion game, player's total score, otherwise 0
        self.totalPlayerScore = dictionary["totalPlayerScore"]

        # long # If game was a dominion game, team rank of the player's total score (e.g., 1-5)
        self.totalScoreRank = dictionary["totalScoreRank"]

        # long # Total dealt crowd control time
        self.totalTimeCrowdControlDealt = dictionary["totalTimeCrowdControlDealt"]

        # long # Total units healed
        self.totalUnitsHealed = dictionary["totalUnitsHealed"]

        # long # Number of tower kills
        self.towerKills = dictionary["towerKills"]

        # long # Number of triple kills
        self.tripleKills = dictionary["tripleKills"]

        # long # True damage dealt
        self.trueDamageDealt = dictionary["trueDamageDealt"]

        # long # True damage dealt to champions
        self.trueDamageDealtToChampions = dictionary["trueDamageDealtToChampions"]

        # long # True damage taken
        self.trueDamageTaken = dictionary["trueDamageTaken"]

        # long # Number of unreal kills
        self.unrealKills = dictionary["unrealKills"]

        # long # Vision wards purchased
        self.visionWardsBoughtInGame = dictionary["visionWardsBoughtInGame"]

        # long # Number of wards killed
        self.wardsKilled = dictionary["wardsKilled"]

        # long # Number of wards placed
        self.wardsPlaced = dictionary["wardsPlaced"]

        # boolean # Flag indicating whether or not the participant won
        self.winner = dictionary["winner"]



class ParticipantTimeline(CassiopeiaDto):
    def __init__(self, dictionary):
        # ParticipantTimelineData # Ancient golem assists per minute timeline counts
        self.ancientGolemAssistsPerMinCounts = ParticipantTimelineData(ParticipantTimelineData(dictionary["ancientGolemAssistsPerMinCounts"]) if isinstance(dictionary["ancientGolemAssistsPerMinCounts"],ParticipantTimelineData) else dictionary["ancientGolemAssistsPerMinCounts"]) if isinstance(ParticipantTimelineData(dictionary["ancientGolemAssistsPerMinCounts"]) if isinstance(dictionary["ancientGolemAssistsPerMinCounts"],ParticipantTimelineData) else dictionary["ancientGolemAssistsPerMinCounts"],ParticipantTimelineData) else ParticipantTimelineData(dictionary["ancientGolemAssistsPerMinCounts"]) if isinstance(dictionary["ancientGolemAssistsPerMinCounts"],ParticipantTimelineData) else dictionary["ancientGolemAssistsPerMinCounts"]

        # ParticipantTimelineData # Ancient golem kills per minute timeline counts
        self.ancientGolemKillsPerMinCounts = ParticipantTimelineData(ParticipantTimelineData(ParticipantTimelineData(dictionary["ancientGolemKillsPerMinCounts"]) if isinstance(dictionary["ancientGolemKillsPerMinCounts"],ParticipantTimelineData) else dictionary["ancientGolemKillsPerMinCounts"]) if isinstance(ParticipantTimelineData(dictionary["ancientGolemKillsPerMinCounts"]) if isinstance(dictionary["ancientGolemKillsPerMinCounts"],ParticipantTimelineData) else dictionary["ancientGolemKillsPerMinCounts"],ParticipantTimelineData) else ParticipantTimelineData(dictionary["ancientGolemKillsPerMinCounts"]) if isinstance(dictionary["ancientGolemKillsPerMinCounts"],ParticipantTimelineData) else dictionary["ancientGolemKillsPerMinCounts"]) if isinstance(ParticipantTimelineData(ParticipantTimelineData(dictionary["ancientGolemKillsPerMinCounts"]) if isinstance(dictionary["ancientGolemKillsPerMinCounts"],ParticipantTimelineData) else dictionary["ancientGolemKillsPerMinCounts"]) if isinstance(ParticipantTimelineData(dictionary["ancientGolemKillsPerMinCounts"]) if isinstance(dictionary["ancientGolemKillsPerMinCounts"],ParticipantTimelineData) else dictionary["ancientGolemKillsPerMinCounts"],ParticipantTimelineData) else ParticipantTimelineData(dictionary["ancientGolemKillsPerMinCounts"]) if isinstance(dictionary["ancientGolemKillsPerMinCounts"],ParticipantTimelineData) else dictionary["ancientGolemKillsPerMinCounts"],ParticipantTimelineData) else ParticipantTimelineData(ParticipantTimelineData(dictionary["ancientGolemKillsPerMinCounts"]) if isinstance(dictionary["ancientGolemKillsPerMinCounts"],ParticipantTimelineData) else dictionary["ancientGolemKillsPerMinCounts"]) if isinstance(ParticipantTimelineData(dictionary["ancientGolemKillsPerMinCounts"]) if isinstance(dictionary["ancientGolemKillsPerMinCounts"],ParticipantTimelineData) else dictionary["ancientGolemKillsPerMinCounts"],ParticipantTimelineData) else ParticipantTimelineData(dictionary["ancientGolemKillsPerMinCounts"]) if isinstance(dictionary["ancientGolemKillsPerMinCounts"],ParticipantTimelineData) else dictionary["ancientGolemKillsPerMinCounts"]

        # ParticipantTimelineData # Assisted lane deaths per minute timeline data
        self.assistedLaneDeathsPerMinDeltas = ParticipantTimelineData(dictionary["assistedLaneDeathsPerMinDeltas"]) if isinstance(dictionary["assistedLaneDeathsPerMinDeltas"],ParticipantTimelineData) else dictionary["assistedLaneDeathsPerMinDeltas"]

        # ParticipantTimelineData # Assisted lane kills per minute timeline data
        self.assistedLaneKillsPerMinDeltas = ParticipantTimelineData(dictionary["assistedLaneKillsPerMinDeltas"]) if isinstance(dictionary["assistedLaneKillsPerMinDeltas"],ParticipantTimelineData) else dictionary["assistedLaneKillsPerMinDeltas"]

        # ParticipantTimelineData # Baron assists per minute timeline counts
        self.baronAssistsPerMinCounts = ParticipantTimelineData(dictionary["baronAssistsPerMinCounts"]) if isinstance(dictionary["baronAssistsPerMinCounts"],ParticipantTimelineData) else dictionary["baronAssistsPerMinCounts"]

        # ParticipantTimelineData # Baron kills per minute timeline counts
        self.baronKillsPerMinCounts = ParticipantTimelineData(dictionary["baronKillsPerMinCounts"]) if isinstance(dictionary["baronKillsPerMinCounts"],ParticipantTimelineData) else dictionary["baronKillsPerMinCounts"]

        # ParticipantTimelineData # Creeps per minute timeline data
        self.creepsPerMinDeltas = ParticipantTimelineData(dictionary["creepsPerMinDeltas"]) if isinstance(dictionary["creepsPerMinDeltas"],ParticipantTimelineData) else dictionary["creepsPerMinDeltas"]

        # ParticipantTimelineData # Creep score difference per minute timeline data
        self.csDiffPerMinDeltas = ParticipantTimelineData(dictionary["csDiffPerMinDeltas"]) if isinstance(dictionary["csDiffPerMinDeltas"],ParticipantTimelineData) else dictionary["csDiffPerMinDeltas"]

        # ParticipantTimelineData # Damage taken difference per minute timeline data
        self.damageTakenDiffPerMinDeltas = ParticipantTimelineData(dictionary["damageTakenDiffPerMinDeltas"]) if isinstance(dictionary["damageTakenDiffPerMinDeltas"],ParticipantTimelineData) else dictionary["damageTakenDiffPerMinDeltas"]

        # ParticipantTimelineData # Damage taken per minute timeline data
        self.damageTakenPerMinDeltas = ParticipantTimelineData(dictionary["damageTakenPerMinDeltas"]) if isinstance(dictionary["damageTakenPerMinDeltas"],ParticipantTimelineData) else dictionary["damageTakenPerMinDeltas"]

        # ParticipantTimelineData # Dragon assists per minute timeline counts
        self.dragonAssistsPerMinCounts = ParticipantTimelineData(dictionary["dragonAssistsPerMinCounts"]) if isinstance(dictionary["dragonAssistsPerMinCounts"],ParticipantTimelineData) else dictionary["dragonAssistsPerMinCounts"]

        # ParticipantTimelineData # Dragon kills per minute timeline counts
        self.dragonKillsPerMinCounts = ParticipantTimelineData(dictionary["dragonKillsPerMinCounts"]) if isinstance(dictionary["dragonKillsPerMinCounts"],ParticipantTimelineData) else dictionary["dragonKillsPerMinCounts"]

        # ParticipantTimelineData # Elder lizard assists per minute timeline counts
        self.elderLizardAssistsPerMinCounts = ParticipantTimelineData(dictionary["elderLizardAssistsPerMinCounts"]) if isinstance(dictionary["elderLizardAssistsPerMinCounts"],ParticipantTimelineData) else dictionary["elderLizardAssistsPerMinCounts"]

        # ParticipantTimelineData # Elder lizard kills per minute timeline counts
        self.elderLizardKillsPerMinCounts = ParticipantTimelineData(dictionary["elderLizardKillsPerMinCounts"]) if isinstance(dictionary["elderLizardKillsPerMinCounts"],ParticipantTimelineData) else dictionary["elderLizardKillsPerMinCounts"]

        # ParticipantTimelineData # Gold per minute timeline data
        self.goldPerMinDeltas = ParticipantTimelineData(dictionary["goldPerMinDeltas"]) if isinstance(dictionary["goldPerMinDeltas"],ParticipantTimelineData) else dictionary["goldPerMinDeltas"]

        # ParticipantTimelineData # Inhibitor assists per minute timeline counts
        self.inhibitorAssistsPerMinCounts = ParticipantTimelineData(dictionary["inhibitorAssistsPerMinCounts"]) if isinstance(dictionary["inhibitorAssistsPerMinCounts"],ParticipantTimelineData) else dictionary["inhibitorAssistsPerMinCounts"]

        # ParticipantTimelineData # Inhibitor kills per minute timeline counts
        self.inhibitorKillsPerMinCounts = ParticipantTimelineData(dictionary["inhibitorKillsPerMinCounts"]) if isinstance(dictionary["inhibitorKillsPerMinCounts"],ParticipantTimelineData) else dictionary["inhibitorKillsPerMinCounts"]

        # string # Participant's lane (Legal values: MID, MIDDLE, TOP, JUNGLE, BOT, BOTTOM)
        self.lane = dictionary["lane"]

        # string # Participant's role (Legal values: DUO, NONE, SOLO, DUO_CARRY, DUO_SUPPORT)
        self.role = dictionary["role"]

        # ParticipantTimelineData # Tower assists per minute timeline counts
        self.towerAssistsPerMinCounts = ParticipantTimelineData(dictionary["towerAssistsPerMinCounts"]) if isinstance(dictionary["towerAssistsPerMinCounts"],ParticipantTimelineData) else dictionary["towerAssistsPerMinCounts"]

        # ParticipantTimelineData # Tower kills per minute timeline counts
        self.towerKillsPerMinCounts = ParticipantTimelineData(dictionary["towerKillsPerMinCounts"]) if isinstance(dictionary["towerKillsPerMinCounts"],ParticipantTimelineData) else dictionary["towerKillsPerMinCounts"]

        # ParticipantTimelineData # Tower kills per minute timeline data
        self.towerKillsPerMinDeltas = ParticipantTimelineData(dictionary["towerKillsPerMinDeltas"]) if isinstance(dictionary["towerKillsPerMinDeltas"],ParticipantTimelineData) else dictionary["towerKillsPerMinDeltas"]

        # ParticipantTimelineData # Vilemaw assists per minute timeline counts
        self.vilemawAssistsPerMinCounts = ParticipantTimelineData(dictionary["vilemawAssistsPerMinCounts"]) if isinstance(dictionary["vilemawAssistsPerMinCounts"],ParticipantTimelineData) else dictionary["vilemawAssistsPerMinCounts"]

        # ParticipantTimelineData # Vilemaw kills per minute timeline counts
        self.vilemawKillsPerMinCounts = ParticipantTimelineData(dictionary["vilemawKillsPerMinCounts"]) if isinstance(dictionary["vilemawKillsPerMinCounts"],ParticipantTimelineData) else dictionary["vilemawKillsPerMinCounts"]

        # ParticipantTimelineData # Wards placed per minute timeline data
        self.wardsPerMinDeltas = ParticipantTimelineData(dictionary["wardsPerMinDeltas"]) if isinstance(dictionary["wardsPerMinDeltas"],ParticipantTimelineData) else dictionary["wardsPerMinDeltas"]

        # ParticipantTimelineData # Experience difference per minute timeline data
        self.xpDiffPerMinDeltas = ParticipantTimelineData(dictionary["xpDiffPerMinDeltas"]) if isinstance(dictionary["xpDiffPerMinDeltas"],ParticipantTimelineData) else dictionary["xpDiffPerMinDeltas"]

        # ParticipantTimelineData # Experience per minute timeline data
        self.xpPerMinDeltas = ParticipantTimelineData(dictionary["xpPerMinDeltas"]) if isinstance(dictionary["xpPerMinDeltas"],ParticipantTimelineData) else dictionary["xpPerMinDeltas"]



class Rune(CassiopeiaDto):
    def __init__(self, dictionary):
        # long # Rune rank
        self.rank = dictionary["rank"]

        # long # Rune ID
        self.runeId = dictionary["runeId"]



class Player(CassiopeiaDto):
    def __init__(self, dictionary):
        # string # Match history URI
        self.matchHistoryUri = dictionary["matchHistoryUri"]

        # int # Profile icon ID
        self.profileIcon = dictionary["profileIcon"]

        # long # Summoner ID
        self.summonerId = dictionary["summonerId"]

        # string # Summoner name
        self.summonerName = dictionary["summonerName"]



class BannedChampion(CassiopeiaDto):
    def __init__(self, dictionary):
        # int # Banned champion ID
        self.championId = dictionary["championId"]

        # int # Turn during which the champion was banned
        self.pickTurn = dictionary["pickTurn"]



class Frame(CassiopeiaDto):
    def __init__(self, dictionary):
        # list<Event> # List of events for this frame.
        self.events = [Event(e) if not isinstance(e,Event) else e for e in dictionary["events"]]

        # dict<string, # ParticipantFrame>   Map of each participant ID to the participant's information for the frame.
        self.participantFrames = {i:ParticipantFrame(pf) if not isinstance(pf,ParticipantFrame) else pf for i,pf in dictionary["participantFrames"]}

        # long # Represents how many milliseconds into the game the frame occurred.
        self.timestamp = dictionary["timestamp"]



class ParticipantTimelineData(CassiopeiaDto):
    def __init__(self, dictionary):
        # double # Value per minute from 10 min to 20 min
        self.tenToTwenty = dictionary["tenToTwenty"]

        # double # Value per minute from 30 min to the end of the game
        self.thirtyToEnd = dictionary["thirtyToEnd"]

        # double # Value per minute from 20 min to 30 min
        self.twentyToThirty = dictionary["twentyToThirty"]

        # double # Value per minute from the beginning of the game to 10 min
        self.zeroToTen = dictionary["zeroToTen"]



class Event(CassiopeiaDto):
    def __init__(self, dictionary):
        # string # The ascended type of the event. Only present if relevant. Note that CLEAR_ASCENDED refers to when a participants kills the ascended player. (Legal values: CHAMPION_ASCENDED, CLEAR_ASCENDED, MINION_ASCENDED)
        self.ascendedType = dictionary["ascendedType"]

        # list<int> # The assisting participant IDs of the event. Only present if relevant.
        self.assistingParticipantIds = [int(api) if not isinstance(api,int) else api for api in dictionary["assistingParticipantIds"]]

        # string # The building type of the event. Only present if relevant. (Legal values: INHIBITOR_BUILDING, TOWER_BUILDING)
        self.buildingType = dictionary["buildingType"]

        # int # The creator ID of the event. Only present if relevant.
        self.creatorId = dictionary["creatorId"]

        # string # Event type. (Legal values: ASCENDED_EVENT, BUILDING_KILL, CAPTURE_POINT, CHAMPION_KILL, ELITE_MONSTER_KILL, ITEM_DESTROYED, ITEM_PURCHASED, ITEM_SOLD, ITEM_UNDO, PORO_KING_SUMMON, SKILL_LEVEL_UP, WARD_KILL, WARD_PLACED)
        self.eventType = dictionary["eventType"]

        # int # The ending item ID of the event. Only present if relevant.
        self.itemAfter = dictionary["itemAfter"]

        # int # The starting item ID of the event. Only present if relevant.
        self.itemBefore = dictionary["itemBefore"]

        # int # The item ID of the event. Only present if relevant.
        self.itemId = dictionary["itemId"]

        # int # The killer ID of the event. Only present if relevant. Killer ID 0 indicates a minion.
        self.killerId = dictionary["killerId"]

        # string # The lane type of the event. Only present if relevant. (Legal values: BOT_LANE, MID_LANE, TOP_LANE)
        self.laneType = dictionary["laneType"]

        # string # The level up type of the event. Only present if relevant. (Legal values: EVOLVE, NORMAL)
        self.levelUpType = dictionary["levelUpType"]

        # string # The monster type of the event. Only present if relevant. (Legal values: BARON_NASHOR, BLUE_GOLEM, DRAGON, RED_LIZARD, VILEMAW)
        self.monsterType = dictionary["monsterType"]

        # int # The participant ID of the event. Only present if relevant.
        self.participantId = dictionary["participantId"]

        # string # The point captured in the event. Only present if relevant. (Legal values: POINT_A, POINT_B, POINT_C, POINT_D, POINT_E)
        self.pointCaptured = dictionary["pointCaptured"]

        # Position # The position of the event. Only present if relevant.
        self.position = Position(dictionary["position"]) if not isinstance(dictionary["position"],Position) else dictionary["position"]

        # int # The skill slot of the event. Only present if relevant.
        self.skillSlot = dictionary["skillSlot"]

        # int # The team ID of the event. Only present if relevant.
        self.teamId = dictionary["teamId"]

        # long # Represents how many milliseconds into the game the event occurred.
        self.timestamp = dictionary["timestamp"]

        # string # The tower type of the event. Only present if relevant. (Legal values: BASE_TURRET, FOUNTAIN_TURRET, INNER_TURRET, NEXUS_TURRET, OUTER_TURRET, UNDEFINED_TURRET)
        self.towerType = dictionary["towerType"]

        # int # The victim ID of the event. Only present if relevant.
        self.victimId = dictionary["victimId"]

        # string # The ward type of the event. Only present if relevant. (Legal values: SIGHT_WARD, TEEMO_MUSHROOM, UNDEFINED, VISION_WARD, YELLOW_TRINKET, YELLOW_TRINKET_UPGRADE)
        self.wardType = dictionary["wardType"]



class ParticipantFrame(CassiopeiaDto):
    def __init__(self, dictionary):
        # int # Participant's current gold
        self.currentGold = dictionary["currentGold"]

        # int # Dominion score of the participant
        self.dominionScore = dictionary["dominionScore"]

        # int # Number of jungle minions killed by participant
        self.jungleMinionsKilled = dictionary["jungleMinionsKilled"]

        # int # Participant's current level
        self.level = dictionary["level"]

        # int # Number of minions killed by participant
        self.minionsKilled = dictionary["minionsKilled"]

        # int # Participant ID
        self.participantId = dictionary["participantId"]

        # Position # Participant's position
        self.position = Position(dictionary["position"]) if not isinstance(dictionary["position"],Position) else dictionary["position"]

        # int # Team score of the participant
        self.teamScore = dictionary["teamScore"]

        # int # Participant's total gold
        self.totalGold = dictionary["totalGold"]

        # int # Experience earned by participant
        self.xp = dictionary["xp"]



class Position(CassiopeiaDto):
    def __init__(self, dictionary):
        # int 
        self.x = dictionary["x"]

        # int
        self.y = dictionary["y"]