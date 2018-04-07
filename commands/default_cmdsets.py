"""
Command sets

All commands in the game must be grouped in a cmdset.    A given command
can be part of any number of cmdsets and cmdsets can be added/removed
and merged onto entities at runtime.

To create new commands to populate the cmdset, see
`commands/command.py`.

This module wraps the default command sets of Evennia; overloads them
to add/remove commands from the default lineup. You can create your
own cmdsets by inheriting from them or directly from `evennia.CmdSet`.

"""
from evennia import default_cmds
from commands.teleport import CmdTeleportExample
from commands.scry import CmdScryExample
from commands.command import Kill
from commands.command import Heal
from commands.spiritdesc import SpiritDesc
from commands.find import CmdFind
from typeclasses.exits import CmdFaster
from typeclasses.exits import CmdSlower
from evennia.contrib.slow_exit import CmdSetSpeed
from commands.combat import CmdAttack
from commands.command import FooBar
from commands.command import Image
from commands.command import Wield
from commands.command import OverLook
from commands.general import CmdInventory
from commands.general import CmdSay
from commands.command import OverGive
from commands.command import OverPose
from commands.command import OverWhisper
from commands.spells import CmdSpell
from commands.cast import CmdCast
from commands.forensic import CmdLastBreath
from commands.sight import CmdSight
from commands.touch import CmdReach
from commands.general import CmdGet
from commands.exorcise import CmdExorcise
from commands.summon import CmdSummon
from commands.inflict import CmdInflict
from commands.invis import CmdInvis
from commands.bless import CmdBless
from commands.hex import CmdHex
from commands.curse import CmdCurse
from commands.enchant import CmdEnchant
from commands.charm import CmdCharm
from commands.use import CmdUse
from commands.fate import CmdFate
from commands.death import CmdDeathTouch
from commands.drain import CmdDrain
from commands.intimidate import CmdIntimidate
from commands.kinetic import CmdKinetic
from commands.ban import CmdBan
from commands.push import CmdPush
from commands.race import CmdRace
from commands.strike import CmdStrike
from commands.stop import CmdStop
from commands.influence import CmdCommand
from commands.project import CmdProject
from commands.bug import CmdBug
from commands.send import CmdSend
from commands.illusion import CmdIllusion
from commands.peek import CmdPeek
from commands.take import CmdTake
from commands.source import CmdSource
from commands.portal import CmdPortal
from commands.jump import CmdJump
from commands.where import CmdWhere
from commands.general import CmdDrop
from commands.general import CmdGive
from commands.freeze import CmdFreeze
from commands.sap import CmdSap
from commands.con import CmdCon
from commands.clone import CmdClone
from commands.make import CmdMake
from commands.heal import CmdHeal
from commands.ressurect import CmdRaise
from commands.shift import CmdShift
from typeclasses.accounts import CmdScrollingHelp
from commands.done import CmdDone
from commands.cast import CmdCast
from commands.slog import CmdSlog
from commands.sheet import Sheet
from commands.dispell import CmdDispell
from commands.meditate import CmdMeditate
from commands.slowtime import CmdSlowtime
from commands.ritual import CmdRitual
from commands.setritual import CmdSetRitual
from commands.stealth import CmdStealth
from commands.astrology import CmdAstrology
from commands.contemplate import CmdContemplate
from commands.charisma import CmdCharisma
from commands.history import CmdHistory

class CharacterCmdSet(default_cmds.CharacterCmdSet):
        """
        The `CharacterCmdSet` contains general in-game commands like `look`,
from commands.history import CmdHistory
        `get`, etc available on in-game Character objects. It is merged with
        the `AccountCmdSet` when an Account puppets a Character.
        """
        key = "DefaultCharacter"

        def at_cmdset_creation(self):
                """
                Populates the cmdset
                """
                super(CharacterCmdSet, self).at_cmdset_creation()
                #
                # any commands you add below will overload the default ones.
                #
                self.add(CmdSetSpeed())
                self.add(OverLook())
                self.add(CmdInventory())
                self.add(OverGive())
                self.add(OverPose())
                self.add(OverWhisper())
                self.add(CmdGet())
                self.add(CmdTeleportExample())
                self.add(CmdScryExample())
                self.add(Kill())
                self.add(Heal())
                self.add(SpiritDesc())
                self.add(CmdFind())
                self.add(CmdFaster())
                self.add(CmdSlower())
                self.add(CmdSetSpeed())
                self.add(CmdAttack())
                self.add(FooBar())
                self.add(Image())
                self.add(Wield())
                self.add(OverLook())
                self.add(CmdSay())
                self.add(OverGive())
                self.add(OverPose())
                self.add(OverWhisper())
                self.add(CmdSpell())
                self.add(CmdCast())
                self.add(CmdLastBreath())
                self.add(CmdSight())
                self.add(CmdReach())
                self.add(CmdExorcise())
                self.add(CmdSummon())
                self.add(CmdInflict())
                self.add(CmdInvis())
                self.add(CmdBless())
                self.add(CmdHex())
                self.add(CmdCurse())
                self.add(CmdEnchant())
                self.add(CmdUse())
                self.add(CmdFate())
                self.add(CmdDeathTouch())
                self.add(CmdDrain())
                self.add(CmdIntimidate())
                self.add(CmdBan())
                self.add(CmdKinetic())
                self.add(CmdPush())
                self.add(CmdRace())
                self.add(CmdStrike())
                self.add(CmdStop())
                self.add(CmdCommand())
                self.add(CmdProject())
                self.add(CmdBug())
                self.add(CmdSend())
                self.add(CmdIllusion())
                self.add(CmdPeek())
                self.add(CmdTake())
                self.add(CmdPortal())
                self.add(CmdSource())
                self.add(CmdJump())
                self.add(CmdWhere())
                self.add(CmdDrop())
                self.add(CmdFreeze())
                self.add(CmdGive())
                self.add(CmdSap())
                self.add(CmdCon())
                self.add(CmdClone())
                self.add(CmdMake())
                self.add(CmdCharm())
                self.add(CmdHeal())
                self.add(CmdRaise())
                self.add(CmdShift())
                self.add(CmdScrollingHelp())
                self.add(CmdCast())
                self.add(CmdSlog())
                self.add(CmdDone())
                self.add(Sheet())
                self.add(CmdDispell())
                self.add(CmdMeditate())
                self.add(CmdSlowtime())
                self.add(CmdRitual())
                self.add(CmdSetRitual())
                self.add(CmdStealth())
                self.add(CmdAstrology())
                self.add(CmdContemplate())
                self.add(CmdCharisma())
                self.add(CmdHistory())

class AccountCmdSet(default_cmds.AccountCmdSet):
        """
        This is the cmdset available to the Account at all times. It is
        combined with the `CharacterCmdSet` when the Account puppets a
        Character. It holds game-account-specific commands, channel
        commands, etc.
        """
        key = "DefaultAccount"

        def at_cmdset_creation(self):
                """
                Populates the cmdset
                """
                super(AccountCmdSet, self).at_cmdset_creation()
                #
                # any commands you add below will overload the default ones.
                #


class UnloggedinCmdSet(default_cmds.UnloggedinCmdSet):
        """
        Command set available to the Session before being logged in.    This
        holds commands like creating a new account, logging in, etc.
        """
        key = "DefaultUnloggedin"

        def at_cmdset_creation(self):
                """
                Populates the cmdset
                """
                super(UnloggedinCmdSet, self).at_cmdset_creation()
                #
                # any commands you add below will overload the default ones.
                #


class SessionCmdSet(default_cmds.SessionCmdSet):
        """
        This cmdset is made available on Session level once logged in. It
        is empty by default.
        """
        key = "DefaultSession"

        def at_cmdset_creation(self):
                """
                This is the only method defined in a cmdset, called during
                its creation. It should populate the set with command instances.

                As and example we just add the empty base `Command` object.
                It prints some info.
                """
                super(SessionCmdSet, self).at_cmdset_creation()
                #
                # any commands you add below will overload the default ones.
                #
