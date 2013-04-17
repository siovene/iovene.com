date: 2006-12-21 13:29:22
slug: common-mistakes-when-approaching-oo-design-class-dependencies
title: Common mistakes when approaching OO design - Class dependencies
category: Software
tags: coding, design

Here we continue with explaining some of the mistakes commonly made in Object
Oriented design, and the good practices that are often ignored. This article is
focused on code maintainability and on improving cooperation with people
working at the same project.

### Encouraging class dependencies

Having a lot of (mutual) dependencies in the code is quite typical of Spaghetti
Code, and it's definitely something we want to avoid, in order to keep our
design neat, improve maintainability and ensure ease of collaboration with
colleagues. What do I mean by "class dependencies"? Let's continue the example
from the last article, and suppose we have a certain class `GuiManager` which,
at some points, wants to generate some reports. Let's introduce now a certain
`ReportManager`, which is a class responsible for generating reports. We have
two types of report: `TableReport`, and `ChartReport`. They look like this:

    class TableReport {
        public:
            void report()  {
                // do something
            }
    };

    class ChartReport {
        public:
            void report()  {
                // do something
            }
    };

This means that the ReportManager will have to look something like this:

    class ReportManager {
        public:
            void reportAll() {
                m_tableReport.report();
                m_chartReport.report();
            }

        private:
            TableReport m_tableReport;
            ChartReport m_chartReport;
    };

There are several problems in this implementation. First of all, If the guy
responsible for the `TableReport` one day wakes up, and decides that the method
`report()` should rather be named `generate()`, he will not only be allowed to
just change that and commit to the repository, but this will break the
`ReportManager`! So after a few hours, the guy responsible for the
`ReportManager` checks out from the repository, builds, and finds out that all
the times he has used the `TableReport` need to be changed. Of course this is
something we don't want to happen.

The usual approach to this, is using an _Abstract Base Class (ABC)_, which is a very robust way to sort out problems like this. Let's see come code:

    class Report {
        public:
            virtual void report() = 0;
    };

    class TableReport : public Report {
        public:
            void report()  {
                // do something
            }
    };

    class ChartReport : public Report {
        public:
            void report()  {
                // do something
            }
    };

Report is our` ABC`, and with it we are literally forcing the people who write
`TableReport` and `ChartReport` to write a method named `report()`. So, this
way we broke one dependency: the `ReportManager` doesn't need to worry about
the way every single report will call the method: it's sure that a method named
`report()` will exist.

There is, tho, another dependency. If somebody writes a new report, say
`XmlReport`, this will need modifications to the `ReportManager`, because our
logic so far implies that the `ReportManager` knows about all the reports. So,
if we're not the maintainers of the `ReportManager` (because maybe it's in some
different library, written by someone else, and we don't have access to the
code), we will have to go ahead and ask the rightful maintainer to modify
the code. Hence, there's an extra dependency, not structural, this time,
but logical. What if the maintainer of the `ReportManager` gave us tools
(read APIs) so that we can _register_ our particular report to the
`ReportManager`? Consider the following code:

    class ReportManager {
        public:
            void registerReport(Report const & r) {
                m_reports.push_back(r);
            }

            void reportAll() {
                std::list::const_iterator iter;
                for(iter = m_reports.begin();
                     iter != m_reports.end();
                     ++iter)
                {
                    iter->report();
                }
            }

            private:
                std::list m_reports;
    };

This way, the `ReportManager` doesn't have to know anything about any `Report`.
